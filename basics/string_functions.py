long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4])

print(long_string[-5:])  # last 5 chars

print(long_string[:-5])  # upto last 5 chars

print(long_string[:4] + " be there")

print("%c is my %s letter and my number %d number is %.3f" %
      ('X', 'favorite', 1, .12578))

print(long_string.capitalize())

print(long_string.find('Floor'))

print(long_string.isalpha)

print(len(long_string))

print(long_string.replace('Floor', 'Ground'))

print(long_string.strip())

quote_list = long_string.split(" ")
print(quote_list)

print(long_string.replace('u', 'U'))