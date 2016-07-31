# reverse position of words in given sentence
# for example,
# input= chelsea are premier league winners
# output= winners league premier are chelsea
# algo: reverse all chars and then reverse chars in each string


def reverse(str, start, end):
    if len(str)==1 or start<0 or start>=end or end>len(str):
        return str

    str = list(str)
    # string = string[::-1]
    while start<end:
        temp = str[start]
        str[start] = str[end]
        str[end] = temp
        start += 1
        end -= 1

    return ''.join(str)


if __name__ == '__main__':
    str = ' chelsea are a top team'
    i=0
    # 1. reverse all chars in given string
    str = reverse(str, 0, len(str)-1)
    # 2. reverse chars in each word
    while i < len(str):
        if str[i] == ' ':
            i += 1
            continue
        j=i
        while i<len(str) and str[i] != ' ':
            i += 1
        str = reverse(str, j, i-1)

    print(str)