#-*- coding:utf-8 -*-
import socket
import threading

def rev(cli):
    '''传入客户端返回的socket对象，循环接受数据'''
    while 1:
        data = cli.recv(1024)
        print data
if __name__ == '__main__':
    #服务端创建IPV4，TCP的socket对象
    ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #bind网址，端口
    addr=('127.0.0.1',8888)
    ser.bind(addr)
    #监听数量为2
    ser.listen(2)
    print 'waiting...'
    #等待连接，这是一个阻塞过程
    cli,addr = ser.accept()
    #如果下面这一句执行，说明阻塞过程完毕
    print 'connected with %s succeed' % str(addr)
    #连接成功后想客户端发送响应
    cli.send('you can talk to me!')
    #创建新线程，调用rev函数，新线程负责接收消息
    t = threading.Thread(target=rev,args=(cli,))
    t.start()
    #主线程继续负责接受用户输入信息并发送
    while True:
        data_me = raw_input() or 'he said nothing'
        cli.send(data_me)

