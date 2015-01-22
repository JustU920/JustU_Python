__author__ = 'zhoumin'
import os

# 获得当前路径
print(os.getcwd())
# 进入目录
os.chdir("../Document")
print(os.getcwd())

# 1. 以只写模式打开文件
# 1.1 文件不存在，自动创建新的文件
# 1.2 文件存在，原文件会先清空
out = open("2222.txt", "w")

# 2. 向文件写入数据
print("file write test", file=out)
print("file write test1", file=out)
print("file write test2", file=out)

# -1.关闭
out.close()


# 一般方法
try:
    data1 = open("3333.txt", "w")
    print("33333...", file=data1)
except IOError as err:
    print("File error: " + str(err))
finally:
    if 'data1' in locals():
        data1.close()

# 使用with关键字来灵活关闭文件
try:
    with open("4444.txt", "w") as data2:
        print("4444....", file=data2)
except IOError as err:
    print("File error: " + str(err))

##################### 腌制数据 #################
# 1. 首先需要导入 import pickle
# 保存一定格式的数据
import pickle
# 保存 wb 只写，二进制
with open("5555.pickle", "wb") as pickleData1:
    pickle.dump([1, 2, 'three'], pickleData1)
# 读取 rb 只读，二进制
with open("5555.pickle", "rb") as pickleData2:
    print(pickle.load(pickleData2)[2])

sortedData = [3, 2, 1, 5, 6, 2, 6, 7]
# 排序
sortedData.sort()
print(sortedData)
print(sorted(sortedData))

# list
# 使用set去除重复项--set中不允许重复
print(set(sortedData))
# 使用字典形式
cleese = {}
cleese['Z'] = [123, 3243, 43213]
cleese['M'] = [567, 888, 43213]
print(cleese['Z'])