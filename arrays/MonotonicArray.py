def isMonotonic(array):
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[0]
            continue
        if breaksDirection(direction, array[i -1, array[i]]):
            return False

    return True

def breakDirection(direction, previous, current):
    diff = current - previous
    if direction > 0:
        return diff < 0
    return diff > 0