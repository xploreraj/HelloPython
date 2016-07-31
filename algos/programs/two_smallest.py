# given an array, find two smallest numbers


def print_two_smallest(arr):
    arr_size = len(arr)
    if arr_size < 3:
        print('Invalid input!')
        return
    min1 = min2 = arr[0]
    for i in range(1, arr_size - 1):
        if arr[i] < min1:
            if arr[i] < min2:
                min1 = min2
                min2 = arr[i]
            elif arr[i] > min2:
                min1 = arr[i]

    if min2 == arr[0]:
        print('No second smallest element. Min element is', min1)
    else:
        print('The min element is {} and second min element is {}'.format(min1, min2))


# driver code
arr = [7, -2, 4, 9, 0, 3]
print_two_smallest(arr)
