def helperMergeSort(arr,start,end):
    #Leafworker
    if start == end:
        return
    mid = (start + end)/2
    helperMergeSort(arr,start,mid)
    helperMergeSort(arr,mid +1,end)
    
    return arr

def mergeSort(arr):
    start = 0
    end = len(arr) - 1
    arr = helperMergeSort(arr,start,end)
    print('Sorted Arrays: ',arr )



