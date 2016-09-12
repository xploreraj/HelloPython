# functional programming means - you can pass around functions just like variables or values

# old way
def by_three(x):
    return x % 3 == 0


# new way - anonymous function
lambda x: x % 3 == 0

'''
When we pass the lambda to filter, filter uses the lambda to determine
what to filter, and the second argument (my_list, which is just the numbers 0 – 15)
is the list it does the filtering on.
'''

my_list = range(16)
print(list(filter(lambda x: x % 3 == 0, my_list)))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(list(filter(lambda x: x is 'Python', languages)))

'''
print out only the squares that are between 30 and 70 (inclusive)
'''
squares = [x ** 2 for x in range(1, 11)]
print(list(filter(lambda x: 30 <= x <= 70, squares)))
