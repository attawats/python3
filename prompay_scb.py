money = float(input('Input Money = '))
def checkfee(money):
    if money <= 5000:
        return 0
    elif 5000  < money <= 30000:
        return 2
    elif 30000 < money < 100000:
        return 5
    else:
        return 10
print(money)
print('fee = ',checkfee(money))