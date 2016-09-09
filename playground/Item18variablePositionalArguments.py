def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

log('My numbers are', [1, 2])
log('Hi there', [])

def log_optional(message, *values):  # The only difference
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

log_optional('My numbers are', 1, 2)
log_optional('Hi there')  # Much better

favorites = [7, 33, 99]
log_optional('Favorite colors', *favorites)


def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)


def log_seq(sequence, message, *values):
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, values_str))

log_seq(1, 'Favorites', 7, 33)      # New usage is OK
log_seq('Favorite numbers', 7, 33)  # Old usage breaks