def insertioSort(A):
    for i in range(0, len(A)-1):
        temp = A[i]
        red = i-1
        while red >=0 and A[red] > temp:
            A [red + 1] = A[red]
            red = red -1
            A[red + 1] = temp
    return A
 
print(insertioSort([2,1,9,2,7]))