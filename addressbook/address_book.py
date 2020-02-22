import os  # 调用os.system('clean')清屏
import pickle  # 生成并保存数据文件

restart = True

addressfile = 'c:\\Users\\vampi\\Desktop\\address.data'

ad = {}
# 文件存在且不为空
if os.path.exists(addressfile) and os.path.getsize(addressfile):
    with open(addressfile, 'rb') as f:
        ad = pickle.load(f)
else:
    with open(addressfile, 'wb') as f:
        pickle.dump(ad, f)


def clear():
    os.system('cls')


def title():
    print('电话簿程序    请输入序号选择对应功能')
    print(' ')


def menu_1():
    print('1：新建联系人')
    print('2：搜索联系人')
    print('3：查看所有')
    print('4：退出程序')


def create():
    while 1:
        clear()
        title()
        print('输入信息')
        name = input('姓名:')
        tel = input('电话:')
        email = input('email:')
        ad[name] = [tel, email]
        clear()
        title()
        print('存入信息：', end='')
        print('姓名：{}\n电话：{}\n邮箱：{}'.format(name, ad[name][0], ad[name][1]))
        print('是否确定保存？(y/n)')
        enter = input()
        if enter == 'n':
            del ad[name]
            name = 'NULL'
            break
        elif enter == 'y':
            name = 'NULL'
            f = open(addressfile, 'wb')
            pickle.dump(ad, f)
            f.close()
            break
        else:
            print('输入错误，请重试！按enter继续')
            input()


def show():
    clear()
    title()
    f = open(addressfile, 'rb')
    ad = pickle.load(f)
    f.close()
    i = 1
    for a in ad:
        print('{}:姓名：{}  电话：{}  邮箱：{}'.format(i, a, ad[a][0], ad[a][1]))
        i += 1
    print('显示完成，enter继续')
    input()


def search():
    f = open(addressfile, 'rb')
    ad = pickle.load(f)
    f.close()
    while 1:
        clear()
        title()
        if len(ad) == 0:
            print('没有记录,按enter返回')
            input()
            break
        else:
            print('请输入姓名：')
            search_name = input('姓名：')
            if search_name in ad:
                print('姓名：{}\n电话：{}\n邮箱：{}'.format(search_name,
                                                   ad[search_name][0], ad[search_name][1]))
                print('\n是否想进行修改或删除？(d/n,删除/取消并返回)')
                modify = input()
                if modify == 'd':
                    del ad[search_name]
                    f = open(addressfile, 'wb')
                    pickle.dump(ad, f)
                    f.close()
                    break
                elif modify == 'n':
                    break
                else:
                    print('enter error')
            else:
                print('查无此人，按enter继续')
                input()
                break


while restart:
    clear()
    title()
    menu_1()

    choose = input()
    if choose == '1':
        create()
    elif choose == '2':
        search()
    elif choose == '3':
        show()
    elif choose == '4':
        restart = 0
    else:
        print('输入错误，按enter继续')
