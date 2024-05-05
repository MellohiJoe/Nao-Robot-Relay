# coding=utf-8
from src.Bot1.BotEvents import BotEvents
import src.Bot1.modules as mod
from socket import *


class Caller(BotEvents):

    def __init__(self):
        BotEvents.__init__(self)
        self.tcp_socket = None
        self.connectIp = mod.remoteIP
        self.connectPort = mod.TcpPort

    # 创建tcp连接服务器
    def init_connect(self):
        try:
            tcp_socket = socket(AF_INET, SOCK_STREAM)
            ip_port = (self.connectIp, self.connectPort)
            tcp_socket.connect(ip_port)
            self.tcp_socket = tcp_socket
            mod.tts.say('连接成功')
        except Exception as e:
            print(e)

    # 发送消息
    def sendMsg(self):
        try:
            send_str = '收到'
            self.tcp_socket.send(send_str.encode('utf-8'))
            self.tcp_socket.close()
        except Exception as e:
            print(e)

    # 创建tcp服务器并发送消息
    def send(self):
        try:
            self.sendMsg()
        except Exception as e:
            print(e)

    def call_friend(self):
        print 'DEBUG 发送'
        self.init_connect()
        self.send()
        print 'DEBUG 发送完成'
