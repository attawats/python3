def celsius_to_fah(celsius):
    return (celsius * 9 / 5) + 32

def temperature_table(): #void function on c java
    for c in range(0, 105, 5):
        f = celsius_to_fah(c)
        print('{}C = {}F'.format(c,f))
    #return None

def menu():
    print('1. convert Celcius to fahrenheit')
    print('2. display temperature table')
    n = input('enter choice: ')
    if n == '1':
        celcius = int(input('enter degree in celcius '))
        print('{}C = {}F'.format(celcius,celsius_to_fah(celcius)))
    elif n == '2':
        temperature_table()

# f = celsius_to_fah(100)
# print(f)
# a = temperature_table() # in python resent None 
# print(a)
menu()