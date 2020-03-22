def is_even (n):
    return True if n % 2 == 0 else False  #same language speak
    #if n % 2 == 0 :
    #    return True
    #else:
    #    return False 
def is_odd(n):
    return not(is_even(n))
    #if n % 2 == 1 :
    #   return True
    #else:
    #   return False
print(is_even(8))
print(is_odd(5))