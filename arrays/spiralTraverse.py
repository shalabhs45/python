def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol +1):
            result.append(array[startRow][col])
        
        for row in range(startRow + 1, endRow +1):
            result.append(array[row][endCol])
        
        for col in reversed(range(startCol, endCol)):
            if startCol == endRow:
               break
            result.append(array[endRow][col])
