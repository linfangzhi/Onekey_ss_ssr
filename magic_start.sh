#!/usr/bin/env bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

#编译并启用BBR魔改
startbbrmod_nanqinlang(){
	remove_all
    yum install -y make gcc
    mkdir bbrmod && cd bbrmod
    wget -N --no-check-certificate https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/bbr/centos/tcp_nanqinlang.c
    echo "obj-m := tcp_nanqinlang.o" > Makefile
    make -C /lib/modules/$(uname -r)/build M=`pwd` modules CC=/usr/bin/gcc
    chmod +x ./tcp_nanqinlang.ko
    cp -rf ./tcp_nanqinlang.ko /lib/modules/$(uname -r)/kernel/net/ipv4
    insmod tcp_nanqinlang.ko
    depmod -a
	echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
	echo "net.ipv4.tcp_congestion_control=nanqinlang" >> /etc/sysctl.conf
	sysctl -p
	echo -e "暴力！魔改版BBR启动成功！"
}

#############系统检测组件#############
startbbrmod_nanqinlang

