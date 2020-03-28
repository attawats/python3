# s = 'rain'
# t = "bow"
# print(s)
# print(t)
# print(s + t)
# print('-' * 10)
# line = '*' * 10
# print(line)
# a = s + t 
# print(a) 
# print('i' not in a) #that is check str i in a by a= rainbow 
#that have  'i' in a and 'i' not in a 

# sliceing
def slice():
    r = '0123456'
    s = 'rainbow'
    print(s[0])
    print(s[0:4]) #start:stop
    print(s[0:4:2]) #start:stop:step
    print(s[0::2]) #start:stop:step if dont have stop , stop is finish 
    print(s[6])
    print(s[-1]) #count backword
    print(s[-3:])
    print(s[-7:-3])
    print(s[::-1]) #reverse string

def print_string(s):
    for i in range(len(s)):
        print('{:>3}'.format(i), end = '')
    print()
    for i in range(-len(s),0 ,1):
        print('{:>3}'.format(i), end = '')
    print()
    for j in s: # sequence type (for each)
        print('{:>3}'.format(j), end = '')
    print()

slice()
#print_string('rainbow')