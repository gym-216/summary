# 数据类型：基本类型 和 容器类型(集合类型)

# 基本类型：数值、布尔、空值、字符串

# 集合类型：有序集合(列表list和元组tuple)、无序集合(字典dict和集合set)

# 不可变类型：数值、字符串、元组tuple

# 可变类型：列表list、字典dict、集合set


# 数值：整型、浮点型、复数
a = 100        		# 整型
print(a)			# 100
print(type(a))		# <class 'int'>

b = 100.0			# 浮点型
print(b)			# 100.0
print(type(b))		# <class 'float'>

c = 1 + 2j			# 复数
print(c)			# (1+2j)
print(type(c))		# <class 'complex'>


# 布尔：仅两个值 True/False    注意大小写
# flag =  true  ->  NameError: name 'true' is not defined
# flag =  false ->  NameError: name 'false' is not defined
flag =  True
print(flag)			# True
print(type(flag))	# <class 'bool'>

flag = False
print(flag)			# False
print(type(flag))	# <class 'bool'>


# 空值: None
null = None
print(null)			# None
print(type(null))	# <class 'NoneType'>


# 字符串
str = 'hello'
print(str)			# hello
print(type(str))	# <class 'str'>


# 列表list：有序可重复 方括号[]
list = [1,2,3,4,5,6,7]
print(list)					# [1, 2, 3, 4, 5, 6, 7]
print(type(list))			# <class 'list'>


# 元组tuple：有序可重复 小括号()
tuple = (1,2,3,4,5,6,7)
print(tuple)				# (1, 2, 3, 4, 5, 6, 7)
print(type(tuple))			# <class 'tuple'>


# 字典dict：无序不重复 花括号{}  键值对key-value
dict = {'name':'gym','age':18}
print(dict)					# {'name': 'gym', 'age': 18}
print(type(dict))			# <class 'dict'>


# 集合set： 无序不重复 花括号{}   可通过花括号{}或set()函数创建集合set
set = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(set)					# {'Zhihu', 'Google', 'Runoob', 'Facebook', 'Baidu', 'Taobao'}
print(type(set))			# <class 'set'>


# 整型补充
# 整数：正整数、0、负整数
a = 1				# 正整数
print(a)			# 1
print(type(a))		# <class 'int'>

b = 0
print(b)			# 0
print(type(b))		# <class 'int'>

c = -1				# 负整数
print(c)			# -1
print(type(c))		# <class 'int'>

# 进制
a = 5				# 十进制
print(a)			# 5
print(type(a))		# <class 'int'>

b = 0b0101			# 二进制 前缀0b/0B
print(b)			# 5
print(type(b))		# <class 'int'>

c = 0x5				# 十六进制 前缀0x/0X
print(c)			# 5
print(type(c))		# <class 'int'>
	
d = 0o5				# 八进制 前缀0o/0O
print(d)			# 5
print(type(d))		# <class 'int'>


# 浮点型补充

# 字符串补充

