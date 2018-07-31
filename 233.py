import os
import socket
import time


def get_host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def make_config_file():
    content1 = 'API_INTERFACE = \'mudbjson\'\nUPDATE_TIME= 6\n'
    content2 = 'SERVER_PUB_ADDR = \'{}\''.format(get_host_ip())
    content3 = '''\nMUDB_FILE = 'mudb.json'\nMYSQL_CONFIG = 'usermysql.json'\nMUAPI_CONFIG = 'usermuapi.json'
    '''
    content_all = content1 + content2 + content3
    print('your ip is:{}'.format(get_host_ip()))
    with open('userapiconfig.py', 'w')as file:
        file.write(content_all)


os.system('clear')
a = '443 444'
key = '3141592654'
set_speed = ''
os.system('yum -y install python-setuptools && easy_install pip')
os.system('yum -y install wget')
print('安装SS')
os.system('pip install shadowsocks')
print('安装SSR')
os.system('yum -y install unzip')
os.chdir('/root/vultr-onekey-ss-ssr')
os.system('unzip SSRR.zip')
os.chdir('/root/vultr-onekey-ss-ssr/shadowsocksr')
os.system('bash initcfg.sh')
make_config_file()
os.system('python mujson_mgr.py -a -p 8848 -k {key}'.format(key=key))
os.system('python mujson_mgr.py -a -p 80 -o http_simple -k {key}'.format(key=key))
os.system('python mujson_mgr.py -a -p 8080 -o http_simple -k {key}'.format(key=key))
os.system('firewall-cmd --zone=public --add-port=80/tcp --permanent')
os.system('firewall-cmd --zone=public --add-port=8080/tcp --permanent')
os.system('firewall-cmd --zone=public --add-port=8848/tcp --permanent')
os.system('firewall-cmd --zone=public --add-port=8848/udp --permanent')
os.system('firewall-cmd --zone=public --add-port=8842/tcp --permanent')
for i in range(int(a[0]), int(a[-1])):
    os.system('python mujson_mgr.py -a -p {port} -k {key} {set_speed}'.format(port=i, key=key, set_speed=set_speed))
    os.system('firewall-cmd --zone=public --add-port={}/tcp --permanent'.format(i))
    os.system('firewall-cmd --zone=public --add-port={}/udp --permanent'.format(i))
os.system('firewall-cmd --reload')
os.system('chmod +x /etc/rc.d/rc.local')
os.system('chmod +x /root/vultr-onekey-ss-ssr/shadowsocksr/run.sh')
with open('/etc/rc.d/rc.local', 'a')as file:
    # 开机自启
    conten01 = '''ssserver -p 8842 -k {key} -m aes-256-cfb -d start\n
                /root/vultr-onekey-ss-ssr/shadowsocksr/run.sh\n
                /root/vultr-onekey-ss-ssr/magic_start.sh'''.format(key=key)
    file.write(conten01)
os.system('clear')
os.system('chmod +x /etc/rc.d/rc.local')
os.chdir('/root/vultr-onekey-ss-ssr')
os.system('chmod +x ./magic_bbr.sh')
os.system('chmod +x ./magic_start.sh')
os.system('cp ./magic_bbr.sh ..')
os.system('chmod +x ./bbr.sh && ./bbr.sh')  # BBR
print('完成')
