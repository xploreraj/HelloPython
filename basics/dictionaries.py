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

print(super_villains.keys())
print(super_villains.values())
print(len(super_villains))

for key in super_villains:
    print(super_villains[key])

print(super_villains.get('notexist')) # keyerror
print(super_villains['notexist'])

#
# Formatting
#

hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'I want %(count)d copies of %(word)s!' % hash
print(s)