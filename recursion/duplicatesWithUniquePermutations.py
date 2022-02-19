def uniquePermutation(arr):
    result = []

    def helper(arr, i):
        #base case:
        if i == len(arr):
            print("0.result", result)
            result.append(arr[:])
        else:
            #Recursive Case
            hmap = {}
            print("1. Map", hmap)
            for pick in range(i, len(arr)):
                if arr[pick] not in hmap:
                   hmap[arr[pick]] =1
                   print("2. Map", hmap)
                   print("3. Arr", arr)
                   arr[pick], arr[i] = arr[i], arr[pick]
                   print("4. Arr", arr)
                   helper(arr, i+1)
                   print("5. Arr", arr)
                   arr[pick], arr[i] = arr[i], arr[pick]
                   print("6. Arr", arr)
    helper(arr,0)

    return result

uniquePermutation([1,1,2])