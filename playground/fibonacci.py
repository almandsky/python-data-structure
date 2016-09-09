
memory = {}


def fibonacci(n):
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    
    if (n in memory):
        return memory.get(n)
    
    res = fibonacci(n - 1) + fibonacci(n - 2)
    memory[n] = res
    return res

# print(fibonacci(7))

for i in range(101):
    print('fabonacci ' + str(i) + ' is ' + str(fibonacci(i)))



