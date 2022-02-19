def get_permutations(arr):
    # Write your code here
    result = []
    
    def helper(slate, arr):
        print("slate",slate)
        print("arr", arr)
        # Base Case: Leaf Node
        if len(arr) == 0:
            result.append(slate)
        # Internal Node Case
        else:
            for i in range(len(arr)):
                helper(slate + [arr[i]], arr[:i]+arr[i+1:])
    helper([],arr)
    return result
print(get_permutations([1,2,3]))