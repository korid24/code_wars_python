'''I = 1; V = 5; X = 10, L = 50, C = 100; D = 500; M =1000'''
symbArr = [['', '', 'M'], ['M', 'D', 'C'], ['C', 'L', 'X'], ['X', 'V', 'I']]

def make_roman(x, ten, five, one):
    if x == 0:
        return ''
    else:
        dct = [one, one*2, one*3, one + five, five, five+one, five + (one*2), five + (one*3), one + ten, ten]
        return dct[x - 1]

def make_arabic(s, ten, five, one):
    if s == '':
        return 0
    else:
        dct = [one, one*2, one*3, one + five, five, five+one, five + (one*2), five + (one*3), one + ten, ten]
        return dct.index(s) + 1

class RomanNumerals:
    def to_roman(self):
        numArr = [int(i) for i in str(self)]
        output = ''
        for i in range(1, len(numArr) + 1):
            output = make_roman(numArr[-i], *symbArr[-i]) + output
        return output

    def from_roman(self):
        s = self
        divided =[''] * len(symbArr)
        for i in range(len(symbArr)):
            ind = 0
            if len(s) > 1:
                while s[ind] in symbArr[i] and ind < len(s) - 1:
                    ind += 1
                divided[i] = s[:ind]
                s = s[ind:]
        for i in range(len(symbArr)):
            if s in symbArr[i]:
                divided[i] += s
                break
        nums = [1000, 100, 10, 1]
        for i in range(len(divided)):
            nums[i] *= make_arabic(divided[i], *symbArr[i])
        return sum(nums)

print(RomanNumerals.to_roman(1990))
print(RomanNumerals.to_roman(1000))
print(RomanNumerals.to_roman(2897))
print(RomanNumerals.from_roman('XXI'))
print(RomanNumerals.from_roman('MMVIII'))
