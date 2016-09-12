super_villains = {'Fiddler': 'Isaac Brown',
                  'Captain Cold': 'Leonard',
                  'Weather Wizard': 'Mark',
                  'Mirror Master': 'Sam Scudder',
                  'Pied Piper': 'Thomas Peterson'}

print(super_villains)
print(super_villains['Captain Cold'])

del super_villains['Fiddler']

super_villains['Pied Piper'] = 'Hartley Runaway'
super_villains['Pied Piper'] = 'New Hartley'

print(super_villains.get('Pied Piper'))

# tuple of key-value pairs
print(super_villains.items())
# array of keys
print(super_villains.keys())
# array of values
print(super_villains.values())

# key-value pairs
print('printing key-value pairs using for >>>>>>>>>')
for key in super_villains:
    print(key, super_villains[key], sep=': ')


print(len(super_villains))

for key in super_villains:
    print(super_villains[key])

# print(super_villains.get('notexist')) # keyerror
# print(super_villains['notexist'], None)

#
# Formatting
#

comic = {}
comic['word'] = 'garfield'
comic['count'] = 42
s = 'I want %(count)d copies of %(word)s!' % comic
print(s)
print('2nd way >>>>>>>>')
print('I want {} copies of %{}!'.format(comic['count'], comic['word']))