age = 20
name = 'bili'

print('{0} was {1} years old when he wrote this book'.format(name, age), end="\n\n")
print('Why is {0} playing with that python?'.format(name))

# format前面的数字可以省略
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

# 更详细的format()格式用法
print('{0:.3f}'.format(1.0/3))  # 保留小数点后三位

print('{0:_^11}'.format("hello"))  # 下划线填充字符，字符串处于中间

print('{0:=^11}'.format("hello"))

print('{name} wrote {book}'.format(
    name='Swaroop', book='A byte of python'))  # 关键字输出字符串
