def minJumpToReachEnd(points):
    step = 0
    distance = 0
    remain = points
    result = 0
    while remain > 0:
        step = step + 1
        distance = distance + step
        remain = points - distance * 2
    if remain < 0:
        distance = distance - step
        step = step - 1
        remain = points - distance * 2
    
    if remain == 0:
        result = step*2
    elif remain > step * 2:
        result = step*2 + 1
    elif remain > step:
        result = step*2 + 2
    else:
        result = step*2 + 1
    
    return result


print(minJumpToReachEnd(14))    
