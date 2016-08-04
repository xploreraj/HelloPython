'''
Print non-consecutive fibonacci numbers summing up to a given number
'''

# return nearest fibonacci num lesser or equal to argument
def nearest_fibo_num(num):
    a, b = 0, 1
    while True:
        if a + b > num:
            break
        temp = b
        b = a + b
        a = temp
    return b


if __name__ == '__main__':
    num = int(input('Enter number and hit enter: '))
    while num>0:
        f = nearest_fibo_num(num)
        print(f, end=' ')
        num -= f
