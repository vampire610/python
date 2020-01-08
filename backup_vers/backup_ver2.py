import os 
import time

# 1.需要备份的文件和目录将被指定在一个列表中
# 如在Linux下：
source = ['./test']

#target_dir = '/home/vampire/Desktop/python/backup'
target_dir = './backup'

if not os.path.exists(target_dir):
	os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

target = today + os.sep + now + '.zip'

if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created directory',today)

zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
	print('Successful backup to', target)
else:
	print('Backp FAILED')
