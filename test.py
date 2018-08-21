import requests
import json
import socket

codes = '''
** DCID **
1:New Jersey
2:Chicago
3:Dallas
4:Seattle
5:Los Angeles
6:Atlanta
7:Amsterdam
8:London
9:Frankfurt
12:Silicon Valley
19:Sydney
24:Paris
25:Tokyo
39:Miami
40:Singapore

** VPSPLANID **
115:8192 MB RAM,110 GB SSD,10.00 TB BW - -60.00
116:16384 MB RAM,110 GB SSD,20.00 TB BW - -120.00
117:24576 MB RAM,110 GB SSD,30.00 TB BW - -180.00
118:32768 MB RAM,110 GB SSD,40.00 TB BW - -240.00
201:1024 MB RAM,25 GB SSD,1.00 TB BW - -5.00
202:2048 MB RAM,40 GB SSD,2.00 TB BW - -10.00
203:4096 MB RAM,60 GB SSD,3.00 TB BW - -20.00
204:8192 MB RAM,100 GB SSD,4.00 TB BW - -40.00
205:16384 MB RAM,200 GB SSD,5.00 TB BW - -80.00
206:32768 MB RAM,300 GB SSD,6.00 TB BW - -160.00
207:65536 MB RAM,400 GB SSD,10.00 TB BW - -320.00
208:98304 MB RAM,800 GB SSD,15.00 TB BW - -640.00


** OSID **
124:Windows 2012 R2 x64
127:CentOS 6 x64
139:Debian 7 x64 (wheezy)
140:FreeBSD 10 x64
147:CentOS 6 i386
152:Debian 7 i386 (wheezy)
159:Custom
160:Ubuntu 14.04 x64
161:Ubuntu 14.04 i386
164:Snapshot
167:CentOS 7 x64
179:CoreOS Stable
180:Backup
186:Application
193:Debian 8 x64 (jessie)
194:Debian 8 i386 (jessie)
215:Ubuntu 16.04 x64
216:Ubuntu 16.04 i386
230:FreeBSD 11 x64
234:OpenBSD 6 x64
240:Windows 2016 x64
244:Debian 9 x64 (stretch)
245:Fedora 26 x64
252:Ubuntu 17.10 x64
253:Ubuntu 17.10 i386
254:Fedora 27 x64
'''


def list():
    print('查询中')
    c = requests.get('https://api.vultr.com/v1/server/list', headers=key)
    if '200' in str(c):
        status_code = 1
    else:
        status_code = 0
    if status_code == 1:
        info_raw_1 = c.text
        try:
            info_raw = json.loads(info_raw_1)
            for i in info_raw:
                show_list = '********************\n' \
                            '服务器编号：{SUBID}\n' \
                            '国家：{location}\n' \
                            'IP地址：{main_ip}\n' \
                            'root密码：{default_password}\n' \
                            '流量使用：{current_bandwidth_gb}\n' \
                            '服务器状态：{power_status}\n' \
                            '服务器花费：{pending_charges}\n' \
                            'ssh root@{main_ip}\n' \
                            '********************\n'.format(
                    **info_raw[i])
                print(show_list)
        except:
            print(info_raw_1)
    else:
        print('出错')


def create():
    print('代码：', codes)
    DCID = input('请输入地区代码：（东京：25,新加坡：40,）')
    VPSPLANID = input('请输入VPS套餐(5刀：201)')
    OSID = input('请输入系统代码（CentOS 7：167）')
    try:
        input('确定？地区：{}  套餐：{}  系统：{}'.format(DCID, VPSPLANID, OSID))
        url = 'https://api.vultr.com/v1/server/create'
        params = {
            'DCID': DCID,
            'VPSPLANID': VPSPLANID,
            'OSID': int(OSID),
        }
        a = requests.post(url=url, headers=key, data=params)
        if '200' in str(a):
            print('\n@@@@@@@  成功  @@@@@@@！\n')
            print(a.text)
        else:
            print(str(a))
    except:
        print('退出')


def account():
    print('请稍等')
    url = 'https://api.vultr.com/v1/account/info'
    a = requests.get(url=url, headers=key)
    b = a.text
    try:
        c = json.loads(b)
        show = '  账户余额：{balance}\n' \
               '  本月花费：{pending_charges}\n' \
               '上次充值日期：{last_payment_date}\n' \
               '上次充值金额：{last_payment_amount}'.format(**c)
        print(show)
    except:
        print(b)

def destroy(SUBID):
    try:
        input('确定 删除？{}'.format(SUBID))
        print("删除服务器中")
        url = 'https://api.vultr.com/v1/server/destroy'
        params = {'SUBID': int(SUBID)}
        a = requests.post(url=url, headers=key, data=params)
        if '200' in str(a):
            print('\n@@@@@@@  成功  @@@@@@@！\n')
        else:
            print(str(a))
    except:
        print('退出')


def reinstall(SUBID):
    try:
        input('确定 重装？{}'.format(SUBID))
        print("重装服务器中")
        url = 'https://api.vultr.com/v1/server/reinstall'
        params = {'SUBID': int(SUBID)}
        a = requests.post(url=url, headers=key, data=params)
        if '200' in str(a):
            print('\n@@@@@@@  成功  @@@@@@@！\n')
        else:
            print(str(a))
    except:
        print('退出')


def prossce():
    false = 'false'
    true = 'true'
    a = {"201": {"VPSPLANID": "201", "name": "1024 MB RAM,25 GB SSD,1.00 TB BW", "vcpu_count": "1", "ram": "1024",
                 "disk": "25", "bandwidth": "1.00", "bandwidth_gb": "1024", "price_per_month": "5.00",
                 "plan_type": "SSD", "windows": false,
                 "available_locations": [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 19, 24, 25, 39, 40]},
         "202": {"VPSPLANID": "202", "name": "2048 MB RAM,40 GB SSD,2.00 TB BW", "vcpu_count": "1", "ram": "2048",
                 "disk": "40", "bandwidth": "2.00", "bandwidth_gb": "2048", "price_per_month": "10.00",
                 "plan_type": "SSD", "windows": false,
                 "available_locations": [1, 2, 3, 4, 5, 6, 7, 8, 12, 19, 24, 25, 39, 40]},
         "203": {"VPSPLANID": "203", "name": "4096 MB RAM,60 GB SSD,3.00 TB BW", "vcpu_count": "2", "ram": "4096",
                 "disk": "60", "bandwidth": "3.00", "bandwidth_gb": "3072", "price_per_month": "20.00",
                 "plan_type": "SSD", "windows": false,
                 "available_locations": [1, 2, 3, 4, 5, 6, 7, 12, 19, 24, 25, 39, 40]},
         "204": {"VPSPLANID": "204", "name": "8192 MB RAM,100 GB SSD,4.00 TB BW", "vcpu_count": "4", "ram": "8192",
                 "disk": "100", "bandwidth": "4.00", "bandwidth_gb": "4096", "price_per_month": "40.00",
                 "plan_type": "SSD", "windows": false, "available_locations": [2, 4, 5, 6, 25]},
         "205": {"VPSPLANID": "205", "name": "16384 MB RAM,200 GB SSD,5.00 TB BW", "vcpu_count": "6", "ram": "16384",
                 "disk": "200", "bandwidth": "5.00", "bandwidth_gb": "5120", "price_per_month": "80.00",
                 "plan_type": "SSD", "windows": false, "available_locations": [4, 6]},
         "206": {"VPSPLANID": "206", "name": "32768 MB RAM,300 GB SSD,6.00 TB BW", "vcpu_count": "8", "ram": "32768",
                 "disk": "300", "bandwidth": "6.00", "bandwidth_gb": "6144", "price_per_month": "160.00",
                 "plan_type": "SSD", "windows": false, "available_locations": [4]},
         "207": {"VPSPLANID": "207", "name": "65536 MB RAM,400 GB SSD,10.00 TB BW", "vcpu_count": "16", "ram": "65536",
                 "disk": "400", "bandwidth": "10.00", "bandwidth_gb": "10240", "price_per_month": "320.00",
                 "plan_type": "SSD", "windows": false, "available_locations": []},
         "208": {"VPSPLANID": "208", "name": "98304 MB RAM,800 GB SSD,15.00 TB BW", "vcpu_count": "24", "ram": "98304",
                 "disk": "800", "bandwidth": "15.00", "bandwidth_gb": "15360", "price_per_month": "640.00",
                 "plan_type": "SSD", "windows": false, "available_locations": []},
         "115": {"VPSPLANID": "115", "name": "8192 MB RAM,110 GB SSD,10.00 TB BW", "vcpu_count": "2", "ram": "8192",
                 "disk": "110", "bandwidth": "10.00", "bandwidth_gb": "10240", "price_per_month": "60.00",
                 "plan_type": "DEDICATED", "windows": false, "available_locations": [1, 2, 12]},
         "116": {"VPSPLANID": "116", "name": "16384 MB RAM,110 GB SSD,20.00 TB BW", "vcpu_count": "4", "ram": "16384",
                 "disk": "110", "bandwidth": "20.00", "bandwidth_gb": "20480", "price_per_month": "120.00",
                 "plan_type": "DEDICATED", "windows": false, "available_locations": [12]},
         "117": {"VPSPLANID": "117", "name": "24576 MB RAM,110 GB SSD,30.00 TB BW", "vcpu_count": "6", "ram": "24576",
                 "disk": "110", "bandwidth": "30.00", "bandwidth_gb": "30720", "price_per_month": "180.00",
                 "plan_type": "DEDICATED", "windows": false, "available_locations": [12]},
         "118": {"VPSPLANID": "118", "name": "32768 MB RAM,110 GB SSD,40.00 TB BW", "vcpu_count": "8", "ram": "32768",
                 "disk": "110", "bandwidth": "40.00", "bandwidth_gb": "40960", "price_per_month": "240.00",
                 "plan_type": "DEDICATED", "windows": false, "available_locations": [12]}}
    ad = dict()
    for i in a:
        ad[a[i]['VPSPLANID']] = a[i]['name'] + ' - -' + a[i]['price_per_month']
    for i in range(800):
        if str(i) in ad:
            print(str(i) + ':' + ad[str(i)])
        else:
            pass


key = {'API-Key': ''}
while True:
    print('\n\n查询账户信息：1\n'
          '查询VPS状态：2\n'
          '新建服务器：3\n'
          '删除服务器：4\n'
          '重装服务器：5\n')
    getinput = input()
    if getinput == '1':
        account()
    elif getinput == '2':
        list()
    elif getinput == '3':
        create()
    elif getinput == '4':
        a = input('请输入服务器编号')
        destroy(a)
    elif getinput == '5':
        a = input('请输入服务器编号')
        reinstall(a)
    elif getinput == '0':
        break
    else:
        print('出错')
print('\n关闭')
exit()
