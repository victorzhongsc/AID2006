"""
练习:  求100000以内质数之和
提示 time.time()求时间点

单进程做这个任务,计算所用的时间

四个进程做这个任务,  10万分为4份
  1--25000  25001--5000 ....
每个进程求其中一份的质数之和

同理求10个进程完成此任务的时间 10万分为10份
"""
import time
from multiprocessing import Process

# 求函数运行时间的装饰器
def timeis(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("运行时间:",end_time - start_time)
        return res
    return wrapper

# 判断一个数是否为质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# 自定义进程类
class Prime(Process):
    def __init__(self,begin,end):
        super().__init__()
        # 求 从begin --end 范围内质数之和
        self.begin = begin
        self.end = end
    def run(self):
        prime = []
        for i in range(self.begin,self.end):
            if isPrime(i):
                prime.append(i)
        print(sum(prime))

# @timeis
# def prime_sum():
#     prime = []
#     # 逐个判断每个数字是不是质数
#     for i in range(1,100001):
#         if isPrime(i):
#             prime.append(i) # 所有质数加入列表
#     print(sum(prime))
#
# # 运行时间: 25.48908495903015
# prime_sum()

# @timeis
# def process_4():
#     jobs = []
#     # 4次循环
#     for i in range(1,100001,25000):
#         p = Prime(i,i+25000) # 自定义进程类
#         jobs.append(p)
#         p.start()
#     [i.join() for i in jobs]

# 运行时间: 14.783753633499146
# process_4()

@timeis
def process_10():
    jobs = []
    # 10次循环
    for i in range(1,100001,10000):
        p = Prime(i,i+10000) # 自定义进程类
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

# 运行时间: 13.871071100234985
process_10()