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
print('''
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @                                     
    @   vultr 搭建专用 木木小方方 2018-01-30  
    @                                     
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @                                     
    @声明:                                 
    @   本脚本仅供学习，以及在不违反中华人民共和国 
    @ 法律下使用，切勿违反中华人民共和国法律。     
    @                                     
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @ ShadowSocks配置（备用，一般不用）        
    @    加密方式    aes-256-cfb            
    @       端口    8842                   
    @-------------------------------------
    @ ShadowSocksR配置                     
    @       协议    auth_aes128_md5        
    @    加密方式    aes-128-ctr            
    @    混淆方式    tls1.2_ticket_auth     
    @       端口    自行设置                 
    @-------------------------------------
    @将会安装：                             
    @      @ ShadowSocks  (python版)     
    @      @ ShadowSocksR (python版）      
    @      @ Google BBR 加速               
    @-------------------------------------
    @注意事项:                              
    @      端口要用空格分开  如:233 666       
    @      有时候需要重启一遍服务器才能完成加速安装
    @      请耐心等待，最后按Y重启，过一分钟之后就能用啦！
    @             
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ''')
while 1:
    a = input('输入端口范围port\n')
    a = a.split()
    if int(a[0])>int(a[-1]):
        print('端口输入错误！')
    else:
        break
while 1:
    key = input('输入通用密码\n')
    if key:
        break
    else:
        continue

print('请牢记密码，安装程序5秒后开始')
time.sleep(5)
os.system('yum -y install python-setuptools && easy_install pip')
os.system('yum -y install wget')
print('安装SS')
os.system('pip install shadowsocks')
print('安装SSR')
os.system('yum -y install unzip')
os.system('unzip SSRR.zip')
os.chdir('/root/vultr-onekey-ss-ssr/shadowsocksr')
os.system('bash initcfg.sh')
make_config_file()
os.system('python mujson_mgr.py -a -p 8848 -k {key}'.format(key=key))
os.system('firewall-cmd --zone=public --add-port=8848/tcp --permanent')
os.system('firewall-cmd --zone=public --add-port=8842/tcp --permanent')
for i in range(int(a[0]), int(a[-1])):
    os.system('python mujson_mgr.py -a -p {port} -k {key}'.format(port=i,key=key))
    os.system('firewall-cmd --zone=public --add-port={}/tcp --permanent'.format(i))
os.system('firewall-cmd --reload')
os.system('chmod +x /etc/rc.d/rc.local')
os.system('chmod +x /root/vultr-onekey-ss-ssr/shadowsocksr/run.sh')
with open('/etc/rc.d/rc.local','a')as file:
    # 开机自启
    conten01 = 'ssserver -p 8842 -k {key} -m aes-256-cfb -d start\n/root/vultr-onekey-ss-ssr/shadowsocksr/run.sh'.format(key=key)
    file.write(conten01)
os.system('clear')
os.chdir('/root/vultr-onekey-ss-ssr')
os.system('chmod +x ./magic_bbr.sh && ./magic_bbr.sh')# BBR
print('完成')

