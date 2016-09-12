grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('First item: ', grocery_list[0])
grocery_list[0] = 'Green juice'
print(grocery_list[0:3])

other_events = ['Wash car', 'Pick up kids', 'Cash check']
to_do_list = [other_events, grocery_list]
print(to_do_list)
print(to_do_list[1][1])  # second item of second list

# append
grocery_list.append('Onions')
# insert
grocery_list.insert(1, 'Pickle')
print(grocery_list)
# remove
grocery_list.remove('Pickle')
# sort
grocery_list.sort()
print('Sorted: ', grocery_list)
# reverse
grocery_list.reverse()
#
del(grocery_list[4])
print('reverse sorted: ', grocery_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

print(grocery_list)
grocery_list.extend(['cookies', 'ice cream'])
print(grocery_list)


print('Building lists - using List Comprehension >>>>\n')

evens_to_20 = [i for i in range(0,20) if i%2 is 0]
print(evens_to_20)

even_squares = [x**2 for x in range(1,12) if x%2 is 0]
print(even_squares)

# The comprehension should consist of the cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.
cubes_by_four = [x**3 for x in range(1, 11) if x**3 % 4 is 0]
print(cubes_by_four)

# List slicing:
# [start:end:stride] - start inc, end exc, and stride is the gap
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(l[2:9:2]) # from 2 to 8, gap of 2
# every odd element
print(l[::2])
# reversing list
print(l[::-1])