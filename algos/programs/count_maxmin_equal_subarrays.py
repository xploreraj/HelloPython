'''
Given an array of numbers, count the total number of subarrays (consecutive elements)
where max and min values are equal.
Ex: 1,1,3
Ans: 4
Below are subarrays where max and min are same.
1
1
3
1,1
'''


def count_maxmin_equal_subarrays(nums):
    n = len(nums)
    total = 0
    i = 0
    # while i < n:
    #     count = 1
    #     while i+1 < n and nums[i] == nums[i+1]:
    #         i += 1
    #         count += 1
    #     i += 1
    #     total += 1 if count == 1 else (count * (count + 1) / 2)

    g = iter(range(n))
    for i in g:
        count = 1
        print(str(i) + '>>>')
        while i+1 < n and nums[i] == nums[i+1]:
            i = next(g)
            count += 1
        total += count * (count + 1) / 2

    return int(total)

num_arr = [1, 3, 3, 1]
print(count_maxmin_equal_subarrays(num_arr))