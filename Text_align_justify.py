#делим строку на списо с разделителем пробел +
#добавляем слова до тех пор, пока при добавлении следующего слова длина не станет больше заданной, +
#формируем список из получившихся строк +
#Функция которая добавляет дополнительные пробелы применяется ко всем строкам кроме последней
#объединяем строки

def divide(str, l=None):
    words = str.split()
    strArr = []
    processedString = ''
    for word in words:
        if len(processedString + word) > l:
            strArr.append(processedString.strip())
            processedString = word + ' '
        else:
            processedString += word + ' '
    strArr.append(processedString.strip())
    return strArr

def fill(line, l):
    lineArr = line.split()
    if len(lineArr) == 1 or len(line) == l:
        return line
    else:
        spaces = [int(i) for i in list('1' * (len(lineArr) - 1))]
        missingSpaceCount = l - len(line)
        j = 0
        while missingSpaceCount > 0:
            spaces[j] += 1
            missingSpaceCount -= 1
            if j == len(spaces) - 1:
                j = 0
            else:
                j += 1
        spaces.append(0)
        outPutLine = ''
        for i in range(len(lineArr)):
            outPutLine += lineArr[i] + (' ' * spaces[i])
        return outPutLine


def justify(text, width):
    divided = divide(text, width)
    filled = [fill(el, width) for el in divided[:-1]]
    filled.append(divided[-1])
    return '\n'.join(filled)



print(justify('123 45 6', 7))
