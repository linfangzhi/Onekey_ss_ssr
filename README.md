# vultr-onekey-ss-ssr vultr 一键安装脚本
## ONLY for Academic learning！！！
## 只供学习用途，请遵守中华人民共和国法律！报道出了偏差，与本人无关！
## 相关法律资料链接，请遵守。
![](https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/baike/crop%3D0%2C92%2C800%2C528%3Bc0%3Dbaike92%2C5%2C5%2C92%2C30/sign=68cbbe45b8fb43160e50203a1d946a1a/f7246b600c338744be5ef1f25b0fd9f9d62aa0a1.jpg)

## [《中华人们共和国网络安全法》](http://www.law-lib.com/law/law_view.asp?id=547569)

## 特点
* 操作简单
* vultr下没问题
## 注意事项
* vultr请使用**CentOS7系统**，出了偏差不要怪我～～
* 请使用root用户登录
## 使用说明
第一步 使用ssh链接主机
'ssh root@你的IP'

第二步 安装git
`yum -y install git`

第三步 克隆项目
`git clone https://github.com/linfangzhi/vultr-onekey-ss-ssr`

第四步 进入vultr-onekey-ss-ssr目录
`cd vultr-onekey-ss-ssr`

第五步 运行命令
`python onekey.py`

第六步 设置密码和端口

第七步 等待

第八步 按Y重启，搞定！

## 一些说明与参数

### ShadowSocks配置（备用，一般不用）
参数|值
------|-------
加密方式|aes-256-cfb
端口|8842
密码|自定义
### ShadowSocksR配置
参数|值
------|-------
协议|auth_aes128_md5
加密方式|aes-128-ctr
混淆方式|tls1.2_ticket_auth
端口|自定义
密码|自定义
### 将会安装
|安装项目|
|-----|
|ShadowSocks   (python版)|
|ShadowSocksR  (python版)|
|Google BBR 加速|


### 注意事项:
* 端口要用空格分开  如:233 666
* 有时候需要重启一遍服务器才能完成加速安装
* 请耐心等待，出现提示后，按Y重启，,完成安装。
# 最后重申，只供学习用途！因为TensorFlow，GOlang，OpenCV等学习网站有时候比较难查询资料，所以为了方便学习。
