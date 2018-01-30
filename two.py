#!/usr/bin/python

# -*- coding: utf-8 -*-


import os
import socket

print("vultr 搭建专用 木木小方方 2018-01-30")
print("要使用root权限")

a = input('输入端口范围port')
a = a.split()
os.system('yum -y update')
print('install git，pip，wget')
os.system('yum -y install python-setuptools && easy_install pip')
os.system('yum -y install wget')
print('安装SS')
os.system('pip install shadowsocks')
print('安装SSR')
os.chdir('/root')
# 这里要注意改变工作路径
os.system('git clone -b manyuser https://github.com/Ssrbackup/shadowsocksr.git')
os.chdir('/root/shadowsocksr')
# 这里要注意改变工作路径
os.system('bash initcfg.sh')


def get_host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def make_config_file():
    content1 = '''API_INTERFACE = 'mudbjson'\nUPDATE_TIME= 60\n
    '''
    content2 = 'SERVER_PUB_ADDR = \'{}\''.format(get_host_ip())
    content3 = '''\nMUDB_FILE = 'mudb.json'\nMYSQL_CONFIG = 'usermysql.json'\nMUAPI_CONFIG = 'usermuapi.json'
    '''
    content_all = content1 + content2 + content3
    print('your ip is:{}'.format(get_host_ip()))
    with open('userapiconfig.py', 'w')as file:
        file.write(content_all)


make_config_file()
os.system('python ./mujson_mgr.py -a -p 8848 -k 3141592654')
os.system('firewall-cmd --zone=public --add-port=8848/tcp --permanent')

for i in range(int(a[0]), int(a[-1])):
    os.system('python mujson_mgr.py -a -p {} -k 3141592654'.format(i))
    os.system('firewall-cmd --zone=public --add-port={}/tcp --permanent'.format(i))
os.system('firewall-cmd --reload')
os.chdir('/root')
os.system(
    'wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh && chmod +x bbr.sh && ./bbr.sh')

