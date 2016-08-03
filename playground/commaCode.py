def commaFormat(values):
    result = ""
    if len(values) == 1:
        result = values[0]
    elif len(values) == 2:
        result = values[0] + ' and ' + values[1]
    elif len(values) > 2:
        length = len(values)
        for i in range(length - 2):
            result += str(values[i]) + ', '
        result += str(values[length - 2]) + ' and ' + str(values[length - 1])
    return result

spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaFormat(spam))

spam = ['longly']
print(commaFormat(spam))

spam = ['you', 'me']
print(commaFormat(spam))

spam = []
print(commaFormat(spam))

spam = [1, 2, 3, 4, 5]
print(commaFormat(spam))