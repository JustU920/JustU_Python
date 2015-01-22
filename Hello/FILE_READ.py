__author__ = 'zhoumin'
import os
######################文件读取#####################
# 获得当前路径
print(os.getcwd())
# 进入目录
os.chdir("../Document")
print(os.getcwd())

# 打开文件前最好先检查文件是否存在
if os.path.exists("1111.txt"):
    print("1111.txt exists!")
else:
    print("you can not open it!")

# 或者打开文件时去做检查
try:
    file = open("12111.txt")
    file.close()
except IOError:
    print("file not exists!")


# 1. 打开文件（文件一定要存在，否则报错）
helloFile = open("1111.txt")
# 2. 读取
print(helloFile.readline(), end='')
# 3. 回到起始位置
helloFile.seek(0)
try:
    for line in helloFile:
        # strip
        print(line, end='')
        # find--不存在，返回-1
        # print(line.find("3"))
except IOError:
    pass
finally:
        # -1. 关闭文件
        helloFile.close()

# 4. 切分
print("")
print("Time=23".split("=")[1])