# point = 1, 7  
# print(point[0])
# print(point[1])
# pointB = (1, 7)
# print(pointB[0])
#can specify tuple 2 form

# th = "thailand", 5, 10, 15
# print(th[1]+th[2]+th[3])
# #can plus but information must same type variable 

# monsters = 'pikachu', 'eevee', 'bulbasaur'
# print(monsters[0])

#tuple is immutable information
def distance(pointA, pointB):
    return ( (pointB[0]-pointA[0])**2 + (pointB[1]-pointA[1])**2 )**0.5 
pointA = 4, 6
pointB = 8, 7
print(distance(pointA,pointB))

#dont use tuple function
def distance2(x1, x2, y1, y2):
    return ( (x2 - x1)**2+(y2 - y1)**2)**0.5
x1 = 4
x2 = 8
y1 = 6
y2 = 7
print(distance2(x1, x2, y1, y2))