'''
Write a program to print all permutations of a given string
Below are the permutations of string ABC.
ABC ACB BAC BCA CBA CAB
permutation is n!

http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

                        ABC
        ABC             BAC             CBA     (swap first, 0, with all others)
    ABC     ACB     BAC     BCA     CBA     CAB (swap second, 1, with all others)

when i==length, print (base cond)

'''


def swap(str_chars, i, j):
    str_chars[i], str_chars[j] = str_chars[j], str_chars[i]


def permute(str_chars, i, n):
    if i is n:
        print(''.join(str_chars))
    else:
        for j in range(i,n):
            swap(str_chars, i, j)
            permute(str_chars, i+1, n)
            swap(str_chars, i, j)  # backtrack. revert change done above and proceed with more changes


# driver
string = 'ABC'
n = len(string)
permute(list(string), 0, n)