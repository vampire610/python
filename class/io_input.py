def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


fuhao = (' ', ',', '.')

print('Rise to vote ,sir. ')
something = 'Rise to vote ,sir. '



for i in fuhao:
	something = something.replace(i, '')

something = something.lower()

print(something)

if is_palindrome(something):
    print('ok')
else:
    print('no')
