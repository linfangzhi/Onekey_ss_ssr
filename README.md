# CentOS 7 酸酸乳 一键安装脚本
## ONLY for academic using！！！
## 只供学习用途，请遵守中华人民共和国法律！报道出了偏差，与本人无关！
## 相关法律资料链接，请遵守。
![](https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/baike/crop%3D0%2C92%2C800%2C528%3Bc0%3Dbaike92%2C5%2C5%2C92%2C30/sign=68cbbe45b8fb43160e50203a1d946a1a/f7246b600c338744be5ef1f25b0fd9f9d62aa0a1.jpg)

## [《中华人们共和国网络安全法》](http://www.law-lib.com/law/law_view.asp?id=547569)

## 特点
* 操作简单
* vultr，Linode下没问题
* 理论上适用于所有**CentOS7系统**服务器
* 添加**云免流**配置
* 添加80和8080端口的http_simple混淆可以用作**云免流**
## 注意事项
* vultr，Linode请使用**CentOS7系统**，出了偏差不要怪我～～
* 请使用root用户登录
## 使用说明

第一步 使用ssh链接主机

`ssh root@你的IP`

第二步 复制一长串代码进终端，回车

`yum -y install wget && wget https://raw.githubusercontent.com/linfangzhi/vultr-onekey-ss-ssr/master/onekey.sh && bash onekey.sh`

第三步 设置端口和密码，端口推荐输入“443 444”

第四步 5秒等待之后，开始安装，去喝杯茶回来就好了，自动重启。

第五步 自己测试一下

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
### ShadowSocksR 默认云免流配置
参数|值
------|-------
协议|auth_aes128_md5
加密方式|aes-128-ctr
混淆方式|http_simple
端口|80和8080
密码|自定义
### 将会安装
|安装项目|
|-----|
|ShadowSocks   (python版)|
|ShadowSocksR  (python版)|
|Google BBR 加速|
|暴力魔改 BBR 加速|
|锐速（加速可以自己选择）|
|80端口与8080端口免流|

**大王卡免流混淆参数：szextshort.weixin.qq.com**

**爱奇艺混淆参数：23.67.167.203,119.39.204.37,111.206.70.132,111.206.70.132**


### 注意事项:
* 端口要用空格分开  如:233 666
# 最后重申，只供学习用途！因为TensorFlow，GOlang，OpenCV等学习网站有时候比较难查询资料，所以为了方便学习。
