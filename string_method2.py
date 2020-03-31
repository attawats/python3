# strip / trim
def demo_strip():
    s = 'thailand'
    t = 'thailand '
    u = t.strip() #remove space before and after but the center not delete
    
    print(s == t)
    print(s == u)

def demo_isdigit(p):
    total = 0
    for c in p :
        # print(c)
        if c.isdigit():
            # print(c)
            total += int(c)
    return total

def remove_non_digit(s):
    t = ''
    for c in s:
        if c.isdigit(): #stroge number
            t += c    
    return t


# plate = '4as 4569'
# print(demo_isdigit(plate))

card_id = '1(25)4-8925-465 164534'
print(remove_non_digit(card_id))