import pickle   #保存数据到文件
import os       #调用os.system('clean')清屏




ad = {}


def create():
    print('enter msg')
    name = input('name:')
    tel = input('tel:')
    email = input('email:')
    ad[name] = [tel, email]
    print(ad[name])


def search():
    if len(ad) == 0:
        os.system('clear')
        print('没有记录')
    else:
        print('ple enter name')
        name = input('name:')
        print(ad[name])
        print('Do you want fix or del this mag?(f/d/n,修改，删除，不操作)')
        modify = input()
        if modify == 'f':
            print()
        elif modify == 'd':
            pass
        elif modify == 'n':
            pass
        else:
            print('enter error')


print('This is an address book')
print('please choose what you want to do')
restart = True
while restart:
    print('1: new contact\n2: search and modify\n3: exit this program')
    choose = input()
    if choose == '1':
        create()
    elif choose == '2':
        search()
    elif choose == '3':
        break
    else:
        print('input error, please re-enter')

print(choose)
