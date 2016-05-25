import random

for x in range(0, 10):
    print(x, ' ', end="")
    if x == 4:
        print()

print('\n')

grocery_list = ['juice', 'tomatoes', 'grapes']

for y in grocery_list:
    print(y)

for x in (1, 2, 3, 4, 5):
    print(x, end=" -> ")

print()
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y], end=" ")
    if x < 2:
        print(end=" and ")

print('\n')
random_num = random.randrange(0, 100)

while random_num != 15:
    print(random_num, end=" ")
    random_num = random.randrange(0, 100)

print('\n')

i = 0;
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    elif i == 9:
        break
    else:
        i += 1
        continue

    i += 1
