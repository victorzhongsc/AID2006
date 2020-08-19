"""
进程间通信演示
"""
from multiprocessing import Process,Queue

# 创建消息队列
q = Queue()

def request():
    name = "Levi"
    passwd = "123"
    # 放入消息队列
    q.put(name)
    q.put(passwd)

def handle():
    # 从消息队列获取内容
    print("Name:",q.get())
    print("Passwd:",q.get())

p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()