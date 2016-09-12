def func(x):
    return (x & x - 1) == 0
x = 17
val = func(x)
print(val)


def foo(a, b, de, ce):
    print(a, b, de, ce)
lst = [0, 1]
dct = {'ce': 3, 'de': 2}
foo(*lst, **dct)

# using atexit module as exit handling mechanism

s = 'abcde'
print(s[::-1])
print(round(3/2))