"""
自定义进程类
"""
from multiprocessing import Process

# 自己定义一个类,让进程执行内容是类中定义的内容
class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__() # 加载父类属性

    # 随便发挥,实现你的功能
    def fun1(self):
        print("假设很复杂步骤1")
    def fun2(self):
        print("假设很凶狠步骤2")
    # 重写run方法,进程功能启动入口
    def run(self):
        # 想实现什么功能写什么
        self.fun1()
        self.fun2()

# 使用自己的类创建进程
p = MyProcess(3)
p.start() # 启动进程->自动运行run方法作为进程执行内容
p.join()











