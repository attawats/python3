def demo():
    print('{}{}'.format('th', 'thailand'))
    print('{:5}|{:15}|'.format('th', 'thailand')) #fill from left #align left
    print('{:<5}|{:<15}|'.format('th', 'thailand')) #fill from left #align left
    print('{:>5}|{:>15}|'.format('th', 'thailand')) #fill from right is full #align right
    print('{:^5}|{:^15}|'.format('th', 'thailand')) #fill from center #align center    print('{:*>5}|{:>15}|'.format('th', 'thailand')) #fill from right is full #align right
    #padding
    print('{:*>5}|{:->15}|'.format('th', 'thailand')) #fill from right is full #align right

def demo_dict():
    menu = {'name': 'mocha', 'price': '40', 'size': 'm'}
    print(menu['name'])
    print('menu name = {} price = {}'.format(menu['name'], menu['price']))
    print('menu name = {name}({size}) price = {price}'.format(**menu)) #same up

def mult_table(n):
    for i in range(1, 13):
        print('{} x {:<2} = {:<3}'.format(n, i, n * i))

def ascii_table():
    for i in range(65, 128):
        print('{0:3} {0:#08b} {0:04o} 0x{0:#x} {0:X} {0:c}'.format(i)) # c is character


# demo()
# demo_dict()
# mult_table(12)
ascii_table()