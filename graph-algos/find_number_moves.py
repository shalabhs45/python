from collections import deque

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):

    if start_row == end_row and start_col == end_col:
        return 0

    board = [[ -1 for _ in range(cols)] for _  in range(rows)]

    print(" board ", board)

    def getNextStep(i,j):
        result = []

        row = i-2
        col = j-1
        if row >= 0 and col >=0 and board[row][col] == -1:
            result.append([row,col])


        row = i-2
        col = j+1
        if row >= 0 and col < cols and board[row][col] == -1:
            result.append([row,col])

        row = i-1
        col = j-2
        if row >= 0 and col >=0 and board[row][col] == -1:
            result.append([row,col])

        row = i-1
        col = j+2
        if row >= 0 and col < cols and board[row][col] == -1:
            result.append([row,col])
        
        row = i+1
        col = j-2
        if row < rows and col >=0 and board[row][col] == -1:
            result.append([row,col])

        row = i+2
        col = j-1
        if row < rows and col >=0 and board[row][col] == -1:
            result.append([row,col])

        row = i+2
        col = j+1
        if(row < rows and col < cols and board[row][col] == -1):
            result.append([row,col])
        #print(result)
        return result

    q = deque()
    q.append([start_row,start_col])
    board[start_row][start_col] = -1
    while q:
        [r,c] = q.popleft()
        for [i,j] in getNextStep(r,c):
            if board[i][j] == -1:
                board[i][j] = board[r][c] + 1 #increment hops
                if i== end_row and j == end_col:
                    return  board[i][j]
                q.append([i,j])

        
    print(board)
    return board[end_row][end_col]



        


