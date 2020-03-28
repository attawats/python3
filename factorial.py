# 5! = 5 * 4 * 3 * 2 * 1
# 0! = 1

# n = 5
# s = 1
# for i in range(1, 9):
#     s = i * s
# print(s)


def factorial (n):
    s = 1
    for i in range(1, n+1):
        s = s * i
    return s
# print(factorial(10))
if __name__ == '__main__':
    n = int(input('Enter Number = '))
    print(factorial(n))