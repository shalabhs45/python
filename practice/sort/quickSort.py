def qShelper(arr, start, end):
    if start >= end:
        return
   # Implement Lomuto's partioning     
    smaller = start # Use randomized version using random number
    # To do random pivot implmentation
    for bigger in range(start+1, end):
        if arr[bigger] < arr [start]:
            smaller = smaller + 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
    arr[start], arr[smaller] = arr[smaller], arr[start]
   # Divide and Solve
    qShelper(arr, start, smaller -1)
    qShelper(arr,smaller+1, end)
    return arr


# Tony Hoare's Partioning - bidirection traversing Theta(n) 
def qShelper2(arr, start, end):
    if start >= end:
        return
    smaller = start + 1
    bigger = end
    while smaller <= bigger:
        if arr[smaller] < arr[start]:
            smaller = smaller + 1
        elif arr[bigger] > arr[start]:
            bigger = bigger - 1
        else: #Both pointers stuck
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
            smaller +=1
            bigger -=1
    arr[start], arr[bigger]  = arr[bigger], arr[start]
      # Divide and Solve
    qShelper2(arr, start, bigger-1) # since pointer crossed each other use bigger -1 as pointer
    qShelper2(arr,bigger+1, end) # taking refernce of bigger pointer taht is the right pointer
    return arr



arr = [8, 5, 2, 9, 5,6,3]
print(qShelper(arr,0,len(arr)-1))
print(qShelper2(arr,0,len(arr)-1))

