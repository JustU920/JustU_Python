__author__ = 'zhoumin'

########################### 列表 ##########################
# 1. 不需要变量标识符
names = ["Tom", "Lily", "Jim", "Fae"]
# 2. 利用0,1,2,3来取值
print("hello " + names[1])
print(len(names))
# 3. names表示的是一个列表，不能同"hello"拼接
print(names)
# 4. 列表末尾添加一项,会把传入的参数当做一项加入
names.append("Lilei")
print(names)
names.append(["121", "2323"])
print(names)
# 5. 列表末尾删除一项,带参数则删除指定项
names.pop()
print(names)
# 6. 列表末尾追加数据项集合
names.extend(["baidu", "google"])
print(names)
# 7. 查找并删除
names.remove("Fae")
print(names)
# 8. 特定位置前面添加一个数据项
names.insert(0, "Kong")
print(names)


# 9. 列表中可以混用各种不同的类型
movies = ["Allern", 1980, "KOBE", 1990, "Mac", 2013]
print(movies)
# 9.1 str + int 不会自动转的，报错
# print(movies[0] + movies[1])
# 10 遍历
for movie in movies:
    print(movie)
i = 0
while i < len(movies):
    print(movies[i])
    i += 1

# 11. 各复杂的列表
movies = ["CHEN", 1990, "LI", 1992, "ZHANG", 1993, ["KONG", 1902, "XIAO", 1009, ["PYTHON", 1909, "JAVA", 1902, ["TEST", 1111]]]]
print(movies[6][4][2])
print(movies)
for movie in movies:
    if isinstance(movie, list):
        for movi in movie:
            if isinstance(movi, list):
                for mov in movi:
                    print(mov)
            else:
                print(movi)
    else:
        print(movie)
# 12.  遍历复杂列表的所有项，方法要先定义
a = testClass()
a.testFunction()

# 13. 注释
"""这些都是注释注释111"""


