shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'zyk'

#Indexing or 'Subscription' operation
print('3',shoplist[3])
print('-1',shoplist[-1])
print('-2',shoplist[-2])

#Slicing on a list 
print ('Item 1 to 3 is', shoplist[1:3])
print ('Item 2 to end is', shoplist[2:])
print ('Item 1 to -1 is', shoplist[1:-1])
print ('Item start to end is', shoplist[:])

#step 步长
print('0,2,4,....', shoplist[::2])
print('0,3,6...', shoplist[::3])
