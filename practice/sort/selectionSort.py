def selectionSort(arr):

    for i in range(0,len(arr)):
        minValue = arr[i]
        minId = i
        for x in range(i+1,len(arr)):
            if arr[x] < minValue:
                minValue = arr[x]
                minId = x
        temp = arr[i]
        arr[i] = arr[minId]
        arr[minId] = temp
    return arr

print(selectionSort([2,1,3,2]))
print(selectionSort([2,1,9,2,7]))

