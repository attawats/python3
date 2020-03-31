import random

def join_demo(): #join is allow use string in tuple can connect
    stations = ("HUA", "SAM", "SIL", "LUM", "KHO", "SIR",
                "SUK", "PET", "RAM", "CUL", "HUI", "SUT",
                "RAT", "LAT", "PHA", "CHA", "KAM", "BAN")
    print(stations)
    print(' --> '.join(stations))
    print(' --> '.join(stations[1:4]))
    print(' --> '.join(stations[3:0:-1]))
    print(' --> '.join(stations[1:4][::-1]))

def password_generator(length):
    # s = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    # print(s)
    # p = random.sample(s, length)
    # print(p)
    # return ''.join(random.sample(s, length))
    return ''.join(random.sample(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"), length))

def replace_demo():
    s = 'password'
    s2 = s.replace('a', '@')
    s3 = s.replace('a', '@').replace('o', '0')
    s4 = s.replace('pass', 'fail') #can replace morn than word
    print(s, s2, s3, s4)




# join_demo()
# for i in range(10):
    # print(password_generator(8))
replace_demo()