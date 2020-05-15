#https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python
from functools import reduce


def next_smaller(n):
    symbol_arr = list(map(int,str(n)))
    if symbol_arr != sorted(symbol_arr):
        immutable = []
        variable = symbol_arr
        for i in range(1, len(symbol_arr)):
            if symbol_arr[-i] < symbol_arr[-i-1]:
                immutable = symbol_arr[:-i-1]
                variable = symbol_arr[-i-1:]
                break

        head = variable[0]
        new_head = max([i for i in variable if i < head])
        variable.remove(new_head)
        variable.sort()
        variable.append(new_head)

        output = reduce(lambda acc,el:acc+el, map(str, immutable + variable[::-1]))

        if int(output) < n and output[0] != '0':
            return int(output)
        else:
            return -1
    return -1


print(next_smaller(100))
