# Dictionary
# 字典是一种可变容器类型可存储任意类型对象
# 字典中每个键值对使用冒号:分割，键值对之间用,分割，字典包含在花括号{}中
# 值可以取任何数据类型，但是键必须是不可变的

tinyDict = {'Name':'kira.wang', 'Age':'25', 12:22}

# ----- 打印字典 ----- #
print("tinyDict:", tinyDict)
print(tinyDict.keys()) # 以列表返回一个列表的所有键
print('Name' in tinyDict.keys())

# ----- 查找字典元素 ----- #
# 访问字典的值
print("tinyDict['Name']:",tinyDict['Name'])

# ----- 添加、修改元素 ----- #
# 向字典添加新内容、修改内容
tinyDict['School'] = "tsinghua" # 添加
tinyDict['Age'] = 25 # 修改为int
# print(type(tinyDict['Age']))

# ----- 删除字典元素 ----- #
del tinyDict['Name'] # 使用del删除
tinyDict.__delitem__(12) # 使用函数删除
print(tinyDict)
# tinyDict.clear() # 清空所有元素
# del tinyDict # 删除字典

# ----- 遍历字典所有元组 -----#
for i in tinyDict.items():
    print(i)
