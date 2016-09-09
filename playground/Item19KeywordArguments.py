def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6

print(remainder(20, 7))
print(remainder(20, divisor=7))
print(remainder(number=20, divisor=7))
print(remainder(divisor=7, number=20))

# SyntaxError: positional argument follows keyword argument
# remainder(number=20, 7) 

# TypeError: remainder() got multiple values for argument 'number'
# remainder(20, number=7)

'''
def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff
'''
'''
def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period
'''
def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff / units_per_kg) / time_diff) * period


weight_diff = 0.5
time_diff = 3
# flow = flow_rate(weight_diff, time_diff)

flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)
pounds_per_hour = flow_rate(weight_diff, time_diff,
                            period=3600, units_per_kg=2.2)

#print('%.3f kg per second' % flow)
print('%.3f kg per second' % flow_per_second)
print('%.3f kg per hour' % flow_per_hour)
print('%.3f pounds per hour' % pounds_per_hour)

pounds_per_hour = flow_rate(weight_diff, time_diff, 3600, 2.2)
print('%.3f pounds per hour' % pounds_per_hour)

