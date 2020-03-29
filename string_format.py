def demo():
    first_name = 'makagun'
    lasy_name = 'gunzz'
    age = 21

    print(first_name, lasy_name, age)
    print('{} {} age: {}'.format(first_name, lasy_name, age)) #{} placeholder
    print('{1} {0} age: {2}'.format(first_name, lasy_name, age)) #positional

def demo_number():
    # n = 2180000564
    # print('{}'.format(n))
    # print('{:,}'.format(n))

    d = 254563.245654
    a = -1234.50
    b = -343.25
    # print('{}'.format(d))
    # print('{:.3f}'.format(d))
    print('{:,.3f}'.format(d))
    print('{:,.3f}'.format(a))
    print('{:,.3f}'.format(b))

    print('-' * 50)
    print('{:15,.3f}'.format(d)) # align right
    print('{:=15,.3f}'.format(a))
    print('{:15,.3f}'.format(b))

    
    


demo_number()