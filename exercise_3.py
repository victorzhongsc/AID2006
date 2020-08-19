"""
练习2: 使用进程池完成
拷贝一个文件夹, (文件夹下全都是普通文件没有子文件夹)

* os.mkdir("xxx") 创建一个新文件夹
* 将目标文件夹下的文件都复制到新文件夹中
  把复制每个文件看做进程池要执行的一件事
"""
from multiprocessing import Pool,Queue
import os

q = Queue() # 消息队列
old_folder = "/home/tarena/FTP/"
new_folder = "./ftp/"

# 拷贝一个文件
def copy(filename):
    fr = open(old_folder+filename,'rb')
    fw = open(new_folder+filename,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        n = fw.write(data) # n表示已经拷贝了多少
        q.put(n) # 放入消息队列
    fr.close()
    fw.close()

# 获取要拷贝的文件的大小
def get_size():
    total_size = 0
    # 累加每个文件大小
    for file in os.listdir(old_folder):
        total_size += os.path.getsize(old_folder+file)
    return total_size # 总大小


def main():
    os.mkdir(new_folder) # 创建新文件夹
    total_size = get_size() # 获取总大小

    # 创建进程池
    pool = Pool()
    # 复制一个文件就用一次copy函数
    for file in os.listdir(old_folder):
        pool.apply_async(func=copy,
                         args=(file,))

    # 获取已经拷贝的大小
    copy_size = 0
    while copy_size < total_size:
        copy_size += q.get()  # 获取已经拷贝字节
        # round(float,n) 保留小数点后 n 位
        print(round(copy_size/total_size*100,2),'%')

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()






