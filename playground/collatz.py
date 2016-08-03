def collatz(number):
    try:
        number = int(number)
        if number % 2 == 0:
            return number
        else:
            return number * 3 + 1
    except ValueError:
        print('Error: Invalid argument.')

print('Please input a number, type \'exit\' to exit')
while True:
    num = input()
    if num == 'exit':
        break
    result = collatz(num)
    if result != None:
        print(result)
    

