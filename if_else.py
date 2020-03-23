print('what area do you want')
print('1.rectangle')
print('2.triangle')
n = input('what number = ')
w = int(input('Weight = '))
h = int(input('Height = '))
def rectangle (w,h):
    area = w * h
    return area
def triangle (w,h):
    area = 0.5 * w * h
    return area
if n == "1":
    print(rectangle(w,h))
else:
    print(triangle(w,h)) 
