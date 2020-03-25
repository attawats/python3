money = float(input('Input Money = '))
def checkfee(money):
    if money > 100000 :
        fee = 10
    elif money > 30000 :
        fee = 5
    elif money > 5000:
        fee = 2
    else:
        fee = 0
    print('fee = ',fee)
checkfee(money)
