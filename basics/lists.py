grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('First item: ', grocery_list[0])
grocery_list[0] = 'Green juice'
print(grocery_list[0:3])

other_events = ['Wash car', 'Pick up kids', 'Cash check']
to_do_list = [other_events, grocery_list]
print(to_do_list)
print(to_do_list[1][1])  # second item of second list

grocery_list.append('Onions')
grocery_list.insert(1, 'Pickle')
print(grocery_list)
grocery_list.remove('Pickle')
grocery_list.sort()
print('Sorted: ', grocery_list)
grocery_list.reverse()
del(grocery_list[4])
print('reverse sorted: ', grocery_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

