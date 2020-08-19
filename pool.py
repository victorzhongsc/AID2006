"""
进程池使用示例
"""
from multiprocessing import Pool
from time import *
import random

# 进程池执行函数
def worker(msg,sec):
    print(ctime(),"---",msg)
    sleep(sec)


# 创建进程池 (进程就已经产生了,父进程退出,进程池会销毁)
pool = Pool(4)

# 向进程池添加时间
for i in range(10):
    msg = "Tedu-%d"%i
    tm = random.randint(1,5)
    # 执行该函数后,事件已经可以在进程池执行了
    pool.apply_async(func=worker,
                     args=(msg,tm))


# 关闭进程池
pool.close()

# 回收进程池
pool.join()