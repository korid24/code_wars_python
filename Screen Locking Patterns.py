#https://www.codewars.com/kata/585894545a8a07255e0002f1/
from itertools import permutations

seps = {
    'AC' : 'B',
    'DF' : 'E',
    'GI' : 'H',
    'AG' : 'D',
    'BH' : 'E',
    'CI' : 'F',
    'AI' : 'E',
    'CG' : 'E',
}
freezed_seps = [item for item in seps.items()]
for key, value in freezed_seps:
    seps[key[::-1]] = value

def check_sep(combination):
    for comb, separator in seps.items():
        if comb in combination:
            if separator not in combination:
                return False
            elif combination.index(separator) > combination.index(comb):
                return False
    return True

def count_patterns_from(firstPoint, length):
    if length == 1:
        return 1
    elif 1 < length < 10:
        points = 'ABCDEFGHI'.replace(firstPoint, '')
        mapped = map(lambda x:firstPoint + ''.join(x), permutations(points, length - 1))
        filtred = filter(check_sep, mapped)
        return len(list(filtred))
    else:
        return 0


print(count_patterns_from("E", 7))
#print(seps['IC'])
