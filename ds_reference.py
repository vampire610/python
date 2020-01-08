print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
#mylist 是指向同一对象的另一个名称
mylist = shoplist

#我购买了第一个项目，将之删除
del shoplist[0]

print('shoplist is ',shoplist)
print('mylist is ', mylist)
#输出中都没有了第一项，可知指向同一对象

print('Copy by making a full slice')
#通过一份完整的切片制作一个新的列表

mylist = shoplist[:]
del mylist[0]

print('mylist', mylist)
print('shoplist', shoplist)

#此时两份列表不同
