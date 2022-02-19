rows = 5
for i in range(1, rows +1):
    for j in range(1, i+1):
        print("*", end =" ")
    print('')

'''
In this example, we will use two for loops in list Comprehension and the final result would be a list of lists.
 we will not include the same numbers in each list. we will filter them using an if condition.
'''

final = [[x,y] for x in [10,20,30] for y in [30,10,50] if x !=y]
print(final)
#[[10, 30], [10, 50], [20, 30], [20, 10], [20, 50], [30, 10], [30, 50]]
