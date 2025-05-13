Ansible klasör yapısını resimdeki gibi başarıyla oluşturduk. Oluşturduğumuz yapı aşağıdaki öğeleri içeriyor:

/etc/ansible/ (Ana Ansible Dizini): Ansible konfigürasyonunu içeren ana dizin

ansible.cfg: Temel Ansible yapılandırma dosyası

inventory/: Yönetilecek sunucuların listesi

hosts.ini: Sunucuların IP ve gruplarını içeren INI dosyası

playbooks/: Ansible görevlerini tanımlayan playbook'lar

webserver_setup.yml: Web sunucusu kurulumu için örnek playbook

group_vars/: Sunucu gruplarına özgü değişkenler

webservers.yml: Web sunucuları için ortak değişkenler

host_vars/: Tek bir sunucuya özgü değişkenler

web1.example.com.yml: Web1 sunucusu için özel değişkenler

ansible_plugins/modules/: Özel Ansible modülleri

ping/ping_module.py: Örnek bir ping modülü

roles/: Playbook'ları işlevsel olarak gruplamak için roller

nginx/: Nginx sunucu rolü

tasks/main.yml: Görevleri tanımlama

handlers/main.yml: Olay işleyicileri

templates/: Şablonlar (nginx.conf.j2, index.html.j2)

defaults/main.yml: Varsayılan değişkenler

templates/: Jinja2 şablon dosyaları

config.json.j2: Örnek bir JSON şablon dosyası

files/: Hedef sunuculara doğrudan kopyalanacak dosyalar

nginx-site.conf: Örnek bir Nginx site yapılandırması

Bu yapıyla Ansible'ı etkili bir şekilde kullanarak sunucu yönetimi, otomatik kurulumlar ve yapılandırmalar gerçekleştirebilirsiniz.