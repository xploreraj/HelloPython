# similar to lists, but we can not change a tuple after its created

pi_tuple = (1, 1, 3, 4, 5, 6)

new_list = list(pi_tuple)
new_list[1] = 2
new_pi_tuple = tuple(new_list)

print(new_pi_tuple)

len(new_pi_tuple)
min(new_pi_tuple)
max(new_pi_tuple)
