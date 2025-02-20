

from select import *
from socket import *

#创建关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

#创建poll对象
p = poll()

#建立地图
fdmap = {s.fileno():s}

#关注IO
p.register(s,POLLIN|POLLERR)

#循环监控IO
while True:
    events = p.poll()
    #遍历events 处理IO
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            #添加新的关注IO
            p.register(c,POLLIN|POLLHUP)
            fdmap[c.fileno()] = c
        elif event & POLLHUP:
            print("客户端退出")
            p.unregister(fd)
            fdmap[fd].close()
            del fdmap[fd]
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            print(data.decode())
            fdmap[fd].send(b"OK")
