python socket 实现点对点聊天
===
socket是什么
----
简单来讲就是对TCP/IP协议集合（对应的OSI为传输层、网络层）的封装，它为我们提供了通往传输层的接口。
```python
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
```
socket.AF_INET->标明此socket为IPV4<br>
socket.SOCK_STREAM->标明此socket为TCP<br>
<br>
接口提供的主要方法有
>s.bind(addr,port)<br>
>s.listen(N)<br>
>s.accept()<br>

注意：s.accept()返回的是另一个socket对象和一个非负整数（如果出错将返回-1），且这一过程是一个阻塞过程，如果没有客户端链接它将一直持续下去<br>
----
功能：服务器与客户端直接聊天（这是不正常的，应该是客户端和客户端通过服务器牵线搭桥聊天），服务器与客户端在接受消息和用户输入消息使用多线程，实现用户可以一边输入消息，一边接受消息<br>
