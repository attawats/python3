def demo1():
    i = 1
    while i <= 10: #in real computer interation 11 round 
        print(i)
        i += 1
    print('bye')
def demo_for():
    for i in range(1, 11):
        print(i)
    print('bye')

def sum_input():
    n = int(input('enter number : '))
    total = 0
    while n != 0 : #while...do 
        total += n
        n = int(input('enter number : '))
    return total    
    # check before run code

#repeat_until
#do..while
def sum_input_repeat_unit():
    total = 0
    while True:
        n = int(input('enter number : '))
        if n != 0:
            total += n
        else:
            break #stop while loop
    print("total = ", total) #use logic in code to stop while loop




# demo1()
# demo_for()
# a = sum_input()
# print(a)
sum_input_repeat_unit()