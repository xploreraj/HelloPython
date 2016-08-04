'''
You are given a set of numbers and a number N. Print all N-digit numbers
that can be formed by the numbers in the given set. The numbers must be
used in the order as in the given set. For the following input

The number set: 4 3 8
N: 3
Sample output:
444
443
448
434
433
438
484
483
488
344
343
348
334
333
338
384
383
388
844
843
848
834
833
838
884
883
888


Solution:
1. for each num, recurse the function
'''

num = []

def func(x, n):
    if n<1:
        print(x)
    else:
        for a in num:
            func(x*10+a, n-1)


if __name__ == '__main__':
    num = [3,4,8]
    N = 4
    func(0, N)