def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # 
    item = [x[0] for x in items]
    weights = [x[1] for x in items]
    list1 = [[-1 for i in range(capacity + 1)] for j in range(len(items) + 1)]

    print(item,weights)
    knapsackutility(item, weights, capacity, len(items),list1)
    print(list1)

def knapsackutility(items, weights, capacity, n, list1):

    if capacity == 0 or n == 0:
        return 0
    if list1[n][capacity] != -1:
        return list1[n][capacity]

    if weights [n -1] > capacity:
        list1[n][capacity] = knapsackutility(items, weights,capacity, n-1,list1)
        return list1[n][capacity]
    else:
        list1[n][capacity] = max(
             items[n-1] + knapsackutility(items, weights,capacity - weights[n-1], n-1,list1),
             knapsackutility(items, weights,capacity, n-1,list1)
         )
        return list1[n][capacity]




knapsackProblem([
  [1, 2],
  [4, 3],
  [5, 6],
  [6, 7]
],10)