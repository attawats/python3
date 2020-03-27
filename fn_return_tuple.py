def price_with_vat(amount):
    vat = amount * 7 / 107 # goods = 100 vat 7% amount = 107
    price = amount - vat #tuple
    t = price, vat
    #return price, vat
    return t

# print(price_with_vat(107))
# a = price_with_vat(200)
# print(type(a))
# print(a)
# print('price = ',a[0])
# print('vat = ',a[1])

p, v = price_with_vat(200)
print(p, v, sep='****') #separate symbol