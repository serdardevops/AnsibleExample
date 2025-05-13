#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = '''
---
module: ping_module
short_description: Uzak sistemlere ping atıp bilgi toplayan bir modül
description:
    - Bu modül uzak sistemlere ping atıp, yanıt süresi ve paket kaybı bilgilerini döndürür.
options:
    count:
        description:
            - Gönderilecek ping paket sayısı
        default: 4
        type: int
    timeout:
        description:
            - Saniye cinsinden ping timeout süresi
        default: 2
        type: int
author:
    - "Örnek Kullanıcı"
'''

EXAMPLES = '''
# Varsayılan değerlerle ping at
- name: Hedef sunucuya ping at
  ping_module:

# Özel değerlerle ping at
- name: 10 paket gönder ve 5 saniye timeout
  ping_module:
    count: 10
    timeout: 5
'''

RETURN = '''
ping_success:
    description: Ping başarılı oldu mu
    type: bool
    returned: always
packet_loss:
    description: Paket kaybı yüzdesi
    type: float
    returned: always
rtt_min:
    description: Minimum yanıt süresi (ms)
    type: float
    returned: on success
rtt_avg:
    description: Ortalama yanıt süresi (ms)
    type: float
    returned: on success
rtt_max:
    description: Maksimum yanıt süresi (ms)
    type: float
    returned: on success
'''

from ansible.module_utils.basic import AnsibleModule
import subprocess
import re

def main():
    module = AnsibleModule(
        argument_spec=dict(
            count=dict(type='int', default=4),
            timeout=dict(type='int', default=2),
        ),
        supports_check_mode=True
    )

    count = module.params['count']
    timeout = module.params['timeout']
    target = module.params.get('target', 'localhost')

    if module.check_mode:
        module.exit_json(changed=False)

    cmd = ['ping', '-c', str(count), '-W', str(timeout), target]
    
    try:
        ping_output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
        ping_success = True
    except subprocess.CalledProcessError as e:
        ping_output = e.output
        ping_success = False

    # Sonuçları ayrıştırma
    result = {
        'ping_success': ping_success,
        'ping_output': ping_output
    }

    if ping_success:
        # Paket kaybı yüzdesini alıyoruz
        packet_loss_pattern = r'(\d+)% packet loss'
        packet_loss_match = re.search(packet_loss_pattern, ping_output)
        if packet_loss_match:
            packet_loss = float(packet_loss_match.group(1))
            result['packet_loss'] = packet_loss

        # RTT değerlerini alıyoruz
        rtt_pattern = r'min/avg/max\S* = (\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)'
        rtt_match = re.search(rtt_pattern, ping_output)
        if rtt_match:
            result['rtt_min'] = float(rtt_match.group(1))
            result['rtt_avg'] = float(rtt_match.group(2))
            result['rtt_max'] = float(rtt_match.group(3))

    module.exit_json(**result)

if __name__ == '__main__':
    main() 