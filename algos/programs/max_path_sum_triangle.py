'''
https://projecteuler.net/problem=18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

t
'''


def max_sum(i, j):
    curr_num = 0
    try:
        curr_num = nums[i][j]
    except IndexError:
        return 0
    return curr_num + max(max_sum(i+1, j), max_sum(i+1, j+1))


nums =  [[3],
        [7, 4],
      [2, 4, 6],
     [8, 5, 9, 3]]

print(max_sum(0,0))