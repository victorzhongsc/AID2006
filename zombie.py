"""
僵尸进程 产生和处理
"""
from multiprocessing import Process
from signal import *

def fun():
    for i in range(3):
        print("我要变僵尸...")

# 忽略子进程退出信号
signal(SIGCHLD,SIG_IGN)

p = Process(target=fun)
p.start()
print("子进程:",p.pid)

# 防止僵尸进程
# p.join()

# 父进程不退出
while True:
    pass