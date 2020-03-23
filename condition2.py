# def ticket(age):
#     if age <= 5 :
#         return 0
#     else:
#         return 100
# def ticket(age):
#     if age <= 5 or age >= 70:
#         return 0
#     else:
#         return 100
#can write function ticker 
def ticket3(age):
    return 0 if age <= 5 or age >= 70 else 100 #ternary 

def ticket2(age,local):
    if (age <= 5 or age >= 70) and local : # if dont write  == True condition local is true
        return 0
    else:
        return 100

def demo(a):
    if a>=10 and a<=20:
        print('good')
    else:
        print('bad')
def demo2(a):
    if 10 <= a <= 20 :
        print('good')
    else:
        print('bad')
# print(ticket(4))
# print(ticket(20))
# print(ticket(80))
# print(ticket2(80,True))
#print(ticket3(100))
demo(15)
demo2(5)