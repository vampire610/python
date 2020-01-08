name = 'Swaroop'

if name.startswith('Swa'):
	print('Yes, the string starts with "Swa"')

if 'a' in name:
	print('a in name')

if name.find('aro') != -1:
	print('aro in name')

delimiter = '_*_'
mylist = ['a','b','c']
print(delimiter.join(mylist))
