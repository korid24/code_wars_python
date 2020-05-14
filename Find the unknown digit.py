#https://www.codewars.com/kata/546d15cebed2e10334000ed9/train/python


def solve_runes(runes):
    to_eval = runes.replace('=', ' == ').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ')
    check = to_eval.replace('=', '').replace('+', '').replace('-', '').replace('*', '').split()
    start = 0
    for el in check:
        if el[0] == '?' and len(el) != 1:
            start = 1
            break

    for i in range(start,10):
        if str(i) not in runes and eval(to_eval.replace('?', str(i))):
            return i
    return -1
