#w = int(input('Weight = '))
#h = int(input('Height = '))
#area = w*h
#print(area)
def rectangle (w,h):
    area = w * h
    return area
def triangle (w,h):
    area = 0.5 * w * h
    return area
#main entry point 
w = int(input('Weight = '))
h = int(input('Height = '))
print(rectangle(w,h)) #order run def function 
print(triangle(w,h))
