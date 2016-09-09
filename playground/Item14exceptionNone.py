# Item 14: Prefer Exceptions to Returning None
'''
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
x, y = 0, 5
result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is wrong!
else:
    print(result)
'''

# first solution by returning tuple
'''
def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

x, y = 0, 5

success, result = divide(x, y)
if not success:
    print('Invalid inputs')
else:
    print(result)
'''

# second solution to return ValueError Exception
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)
