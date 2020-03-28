# def mult (n):
#     for i in range (1, 13):
#         s = n * i
#         print('{} x {} = {} '.format(n, i, s))
# mult(16)

def mult_table (from_n, to_n):
    #nested loop
    for i in range (from_n, to_n + 1):
        for j in range (1, 13):
            s = j * i
            print('{} x {} =  {}'.format(i, j, s))
            #print('{} x {} =  {}'.format(i, j, j * i))
        print('_' * 40)
mult_table(1, 5)