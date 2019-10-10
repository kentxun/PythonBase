# !/usr/bin/env python
# -*- coding:utf-8 -*-

from Queue import Queue
import socket
import threading

# 这是一个最简单的python单例模式（大概就是保证当前类只有一个对象）
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# io数据流，重新封装了一个类，用于对流媒体流的转发
class Iostream(Singleton):

    def __init__(self):
        # 队列存储数据
        # 新建套接字来建立连接
        self.buffer = Queue()
        self.socket = None
        self.address = None
        self.connecting = False
        self.thread = None

    def start(self, host, port):
        self.stop()
        self.connect(host, port)
    # 建立套接字
    def stop(self):
        if self.connecting:
            self.close_fd()

    def write_buffer(self, data):
        # 如果建立连接，将数据存入队列中
        if self.connecting:
            self.buffer.put_nowait(data)
    # 建立连接
    def connect(self, host, port):
        self.set_fd(host, port)
        self.connecting = True
        # 开启一个新线程
        self.thread = threading.Thread(target=self.write_fd)
        self.thread.start()

    def set_fd(self, host, port):
        # 建立socket连接
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = (host, port)

    # 关闭连接
    def close_fd(self):
        self.connecting = False
        self.socket.close()
        self.socket = None
        self.buffer = Queue()

    # 从队列中获取数据，然后发送到相应的地址
    def write_fd(self):
        while self.connecting:
            data = self.buffer.get(block=True)
            self.socket.sendto(data, self.address)

# 代理类
class Proxy(object):

    def __init__(self, port, host="localhost"):
        self.address = (host, port)
        self.buffer_size = 3000
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(self.address)
        # 在这里建立iostream的类对象
        self.iostream = Iostream()

    # socket监听
    def run(self):
        t = threading.Thread(target=self.listen)
        t.start()

    # 利用iostream发送数据
    def write(self, data):
        self.iostream.write_buffer(data)

    # 监听获取数据
    def listen(self):
        while True:
            data, _ = self.socket.recvfrom(self.buffer_size)
            self.write(data)
