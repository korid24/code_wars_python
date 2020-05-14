#https://www.codewars.com/kata/5629db57620258aa9d000014/train/python
import re

def mix(s1, s2):
    symbols = set(re.findall('[a-z]', s1+s2))
    all = []
    for symbol in symbols:
        if s1.count(symbol) > s2.count(symbol):
            all.append([symbol, s1.count(symbol), '1'])
        elif s1.count(symbol) < s2.count(symbol):
            all.append([symbol, s2.count(symbol), '2'])
        else:
            all.append([symbol, s2.count(symbol), '='])
    counts = sorted(list(set([el[1] for el in all])), reverse=True)
    all = [el for el in all if el[1] > 1]
    sorted_alls = []
    for count in counts:
        sorted_alls += sorted([el for el in all if el[1] == count and el[2] == '1'], key=lambda el: el[0])
        sorted_alls += sorted([el for el in all if el[1] == count and el[2] == '2'], key=lambda el: el[0])
        sorted_alls += sorted([el for el in all if el[1] == count and el[2] == '='], key=lambda el: el[0])
    sorted_alls = [el for el in sorted_alls if el]
    output = ''
    for el in sorted_alls:
        output += f'{el[2]}:{el[0]*el[1]}/'
    return output[:-1]

print(mix("Are they here", "yes, they are here"))
