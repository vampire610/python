number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('you win')
        running = False
    elif guess > number:
        print('da le')
    else:
        print('xiao le')

else:
    print(' loop is over')


print('Done')
