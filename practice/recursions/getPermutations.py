def get_permutations(arr):
    # Write your code he
    result = []
    
    def helper(s, i , slate):
        
        # Base case
        
        if i == len(s):
            print('complete',s[:])
            result.append(s[:])
            
        # Internal Node or Leaf Node case
        
        for x in range(i, len(s)):
            print(x,i,' ',slate)
            # When s[x] choosen
            s[x], s[i] = s[i],s[x]
            print("after swap 1", s)
            print(slate)
            slate.append(s[i])
            print(slate)
            helper(s, i+1, slate)
            print(slate)
            slate.pop()
            print(slate)
            s[i],s[x] = s[x],s[i]
            print("after swap 2", s)
            print(slate)
            
    helper(arr,0,[])
    return result


print(get_permutations([1,2,3]))
            