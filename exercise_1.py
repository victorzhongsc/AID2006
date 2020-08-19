"""
练习: 大文件拆分
比如有一个大文件拆分为2份,分别上下两部分拆成一个新文件

要求 : 1. 按照字节大小拆分
    2. 要求上下两部分同时拷贝拆分,不能先做
       做一部分再一部分

思路: 同时---> 进程
   提示--->  getsize()  seek()
"""
from multiprocessing import Process
import os

filename = "./timg.jpg"
size = os.path.getsize(filename) # 获取文件大小

# 如果父进程中打开子进程直接拿来
# 用那么文件偏移量使用的是一个,相互有影响
# 如果子进程中各自打开择,各自使用自己的偏移量没有影响
# fr = open(filename,'rb')

# 复制上半部分
def top():
    fr = open(filename,'rb')
    fw = open("top.jpg","wb")
    n = size // 2 # 一半大小
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
    fr.close()
    fw.close()

# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open("bot.jpg", "wb")
    fr.seek(size//2,0) # 偏移量移动到中间
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

jobs = []
for i in [bot,top]:
    p = Process(target=i)
    jobs.append(p)
    p.start()

# 一起回收进程
[i.join() for i in jobs]