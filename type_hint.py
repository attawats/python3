#type hints

# def alpha(a, b): #dynamic typed 
#     c = a + b
#     print(c)

# def beta(a: str, b: int, c): #dynamic type
#     print(a,b,c)
def bar(a, b) -> str: #tell this what type return function
    return a + b

if __name__ == '__main__':
    # alpha(5,3)
    # alpha('rain','bow')
    # beta('1', 'rain', 7)
    c =bar('5', '5')
    print(c)
    print(type(c))    