#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket   # 用于socket通信
import subprocess
import pymysql # 数据库
import time
import gevent  # 协程库
from gevent import socket, monkey
import logging

from udp_proxy import Iostream, Proxy # 自己封装的数据传输库

monkey.patch_all()

now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
filename = 'mediaServer-' + now + '.log'
# 日志
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(filename)s.%(funcName)s] %(levelname)s %(message)s',
                    datefmt='%c',
                    filename=filename,
                    filemode='w')

play = 'PLAY'  # 播放
switch = 'SWITCH'  # 切屏
stop = 'STOP'  # 停止
sep = 'SE1P'  # 分音
loop = 'SEP'  # 循环

# 初始化全局参数
source_video = None  # 播放源
ip_set = []  # 所有vlc客户端集合
loop_sym = True  # 循环播放控制符号
udp_proxy = None  # udp代理
iostream = Iostream()  # io缓冲层
port = 1234  # vlc client端口号

# 初始化函数
def init():
    global ip_set
    # 建立pymysql
    conn_sql = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='CPEDB')
    logging.info("Conecet sql: host='127.0.0.1', port=3306, user='root', passwd='1234', db='CPEDB'")
    cursor = conn_sql.cursor()
    # 执行查询数据库的命令
    cursor.execute("select ip from Block WHERE Name LIKE 'vlc%'")
    # 记录日志
    logging.info("select ip from Block WHERE Name LIKE 'vlc%'")
    # 获取ip
    ips = cursor.fetchall()  # (('192.168.1.108',), ('192.168.1.125',), ('192.168.1.136',), ('192.168.1.128',))
    conn_sql.commit()
    cursor.close()
    conn_sql.close()
    # 将ip存入列表中
    for i in ips:
        ip = i[0]
        ip_set.append(ip[0])
    logging.info('IPSET : %s' % ip_set)


def getserver(port):
    # 初始化 服务器段socket
    server = socket.socket()
    # 绑定物理机的 ip和端口
    server.bind(('127.0.0.1', port,))
    # 监听
    server.listen(5)
    print('服务套接字已经创建成功')
    logging.info(' Socket is created successfully')
    print('等待客户机连接')
    logging.info('Waiting for connecting')
    # 循环等待接受连接，获取数据，处理请求
    while True:
        conn, address = server.accept()
        handle_request(conn)

# 处理请求（主要功能），根据上面接受的请求处理，每个功能都单独封装函数
def handle_request(conn):
    global loop_sym
    # 获取指令和IP
    ret = str(conn.recv(1024))
    # 数据分割开来
    data = ret.split()
    command = data[0]
    ip = data[1]
    logging.info('Connect successfully and start processing the request')
    logging.info('Now client IP is : %s ' % (str(ip)))
    try:
        # 播放
        if command == play:
            logging.info('Operation is : %s' % command)
            doplay(ip)
        # 停止、切屏、分音、循环
        else:
            # 停止
            logging.info('Operation is : %s' % command)
            if command != sep:
                try:
                    loop_sym = False
                    iostream.stop()
                except Exception, e:
                    logging.warning(e)

            # 切屏
            if command == switch:
                logging.info('Operation is : %s' % command)
                doswitch(ip)

            # 分音
            elif command == sep:
                logging.info('Operation is : %s' % command)
                dosep(ip)

            # 循环
            elif command == loop:
                logging.info('Operation is : %s' % command)
                doloop(ip)

    except Exception, e:
        print(e)
        logging.warning(e)

# 播放功能
def doplay(ip):
    # 之前获取的全局变量
    global source_video, udp_proxy, port, iostream
    # 判断节目源是否为空
    if source_video is None:
        # 需要执行的系统vlc命令，在后台开启媒体流
        source_com = 'vlc /home/mobicents/sample1.mp4 --sout udp:192.168.1.107 --ttl 12 --loop'
        logging.info('Source is : %s ' % source_com)
        # 创建在系统内执行命令的子进程，去执行vlc 命令
        source_video = subprocess.Popen(source_com, shell=True)
        # 这里是优化后的方案，将媒体流绑定1234端口，用于流转发
        udp_proxy = Proxy(1234)
        udp_proxy.run()
    logging.info('To play: %s ' % ip)
    # 将媒体流播放到指定的ip和端口
    iostream.start(ip, port)

# 切换功能
def doswitch(ip):
    global port, iostream
    logging.info('To switch: %s' % ip)
    # 同播放，切换播放流
    iostream.start(ip, port)

# 分音功能，暂时忽略，也是利用的vlc的功能
def dosep(ip):
    global run_video, vlc_instance
    playing_ip = run_video[-1]
    no_audio = playing_ip + "-no-audio"
    no_video = ip + "-no-video"
    logging.info('To sep: video: %s, audio: %s' % (playing_ip, ip))

    vlc_instance.vlm_play_media(no_audio)
    run_video.append(no_audio)
    vlc_instance.vlm_play_media(no_video)
    run_video.append(no_video)
    logging.info('Dosep start successfully')

# 循环= 自定义控制的循环的切换
def doloop(ip):
    try:
        gevent.spawn(run_loop, ip)
    except Exception, e:
        print(e)
        logging.warning(e)

# 从数据获取的 多个终端的ip，从而实现循环
def run_loop(ip):
    global loop_sym, iostream, ip_set, port
    loop_sym = True
    start = ip_set.index(ip)
    num = len(ip_set)
    while loop_sym:
        try:
            to_play = ip_set[start]
            logging.info('run_loop: %s' % to_play)
            iostream.start(to_play, port)
            start += 1
            start %= num
            time.sleep(20)
        except Exception, e:
            logging.warning(e)


if __name__ == '__main__':
    init()
    getserver(1000)
