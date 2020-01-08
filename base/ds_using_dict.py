# ab 是地址簿的缩写 Adress Book

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'zyk': 'aaassda@aa.com',
    'wwj': 'wawkdaf.df'
}
print("zyk's adress is", ab['zyk'])

# delete a key-val
del ab['Larry']
print('\nThere are {} contacts in the adress-book\n'.format(len(ab)))

for name, adress in ab.items():
    print('Contact {} at {}'.format(name, adress))

# add a key & val

ab['aaa'] = 'vvv.ccc'

if 'aaa' in ab:
    print('\naaa\'s adress is', ab['aaa'])
