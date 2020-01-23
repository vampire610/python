import pickle

ad = {}


def create():
    print('enter msg')
    name = input('name')
    tel = input('tel')
    email = input('email')
    ad[name] = [tel, email]
    print(ad[name])


print('This is an address book')
print('please choose what you want to do')
restart = True
while restart:
    print('1: new contact\n2: search and modify\n3: exit this program')
    choose = input()
    if choose == '1':
        create()
    elif choose == '2':
        pass
    elif choose == '3':
        break
    else:
        print('input error, please re-enter')

print(choose)
