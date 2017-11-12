#-*- coding:utf-8 -*-
import socket, threading
from concurrent import futures

def rev(c):
	'''传入客户端的socket对象，循环接受服务端数据'''
	while 1:
		data = c.recv(1024)
		print data
if __name__ == '__main__':
	#创建socket对象
	c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	addr = ('127.0.0.1',8888)
	#阻塞过程
	c.connect(addr)
	#上一步成功后才执行
	print 'connected succeed!'
	#创建新线程，用来接受服务器信息
	t=threading.Thread(target=rev,args=(c,))
	t.start()
	#主线程继续接受用户输入信息，并发送
	while True:
	    word = raw_input() or 'he said nothing'
	    c.sendall(word)
	c.close()
