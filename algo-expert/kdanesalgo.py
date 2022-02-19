def kadanesAlgorithm(array):
    # Write your code here.
     maxSum = array[0]
     currentSum = array[0]

     for x in range(1, len(array)):
         num = array[x]
         currentSum = max(num, currentSum + num)
         maxSum = max(currentSum, maxSum)
     return maxSum        

print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))