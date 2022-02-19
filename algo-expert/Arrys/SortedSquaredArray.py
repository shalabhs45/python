def sortedSquaresArray(array):
    sortedSquares = [ 0 for _ in array]
    left = 0
    right = len(array) -1

    for idx in reversed(range(len(array))):
        left = array[left]
        right = array[right]

        if abs(left) > abs[right]:
            sortedSquares[idx] = left *  left
            left += 1
        else:
            sortedSquares[idx] = right * right
            right -= 1
    
    return sortedSquares