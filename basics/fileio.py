import os
import re

# test_file = open('fileio_test.txt', 'wb')
test_file = open('fileio_test.txt', 'r')

lines = test_file.readlines()
nam = ''
itemAcc = ''
bal = ''
next_line_amt = False
amtRegex = re.compile(r'(?:^[\s]*"([\d]+[\.]?[\d]*)",$)', flags=0)

# print('%s\t%s\t%s' % ('item account id', 'balance', 'account name'))
print('{}\t{}\t{}'.format('item_account_id', 'balance', 'account_name'))

for line in lines:
    if '"amount":' in line:
        next_line_amt = True
        continue
    if next_line_amt:
        amount = amtRegex.search(line)
        bal = amount.group(1)
        next_line_amt = False
        continue
    if '\"name\":' in line:
        nam = line.strip()[9:-2]
        continue
    if 'itemAccountId' and '&amp;itemId' in line:
        itemAcc = line[line.find('itemAccountId') + 14 : line.find('&amp;itemId')]
        print(itemAcc + '\t' + bal + '\t' + nam)
        itemAcc, nam, bal = '', '', ''
    # for end

# print(test_file.mode)

# print(test_file.name)

# test_file.write(bytes('Write me to the file\n', 'UTF-8'))

test_file.close()

# test_file = open('fileio_test.txt', 'r+')
# text_in_file = test_file.read()
# test_file.close()
# print("read data:\n", text_in_file)


# os.remove('fileio_test.txt')
