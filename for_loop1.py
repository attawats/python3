def loop1():
    for i in range(11): # for(i=0;i<11;i++)
        print(i)

def loop2():
    for i in range(1, 11): # for(i=1;i<11;i++)
        print(i)

def loop3():
    for i in range(1, 11, 2): # for(i=1;i<11;i=i+2)
        print(i)
        print('--')
    print('bye!!')

def loop_string():
    s = 'over the rainbow'
    for c in s :
        print(c.upper())

def loop_tuple():
    flower = 'lily', 'jasmine', 'rose', 'ivy'
    for f in flower:
        print(f.capitalize())

def loop_tuple2():
    flower = 'lily', 'jasmine', 'rose', 'ivy'
    for i in range(len(flower)):
        # print(i+1, flower[i], sep='. ')
        print(i+1,'.', flower[i])


# loop3()
# loop_string()
loop_tuple2()