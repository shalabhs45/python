def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(len(arr)-1, i,-1):
            if arr[j-1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            print(j, ' ', arr)
    return arr

print(bubbleSort([2,1,3,2]))
print(bubbleSort([2,1,9,2,7]))