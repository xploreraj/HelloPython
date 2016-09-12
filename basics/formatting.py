print('Python {} fun'.format('is'))
print('{} {} {}'.format('Python', 'is', 'fun'))

print('Python {0} {1} and {1} {0} awesome!'.format('is', 'fun'))

version = 3
print('Python {} is fun'.format(version))

print()
# {x:y} => x means argument number, and y means padding (left padding by default)
print('{0:10} | {1:8}'.format('Vegetable', 'Quantity'))
print('{0:10} | {1:8}'.format('Asparagus', 3))
print('{0:10} | {1:8}'.format('Onion', 5))

print()

# Alignment control and float

print('{0:10} | {1:>12}'.format('Vegetable', 'Quantity'))
print('{0:10} | {1:<12}'.format('Asparagus', 3))
print('{0:10} | {1:^12.3f}'.format('Onion', 5.2446))

