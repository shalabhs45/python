sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]

sampleSet.update(sampleList)
print(sampleSet)

#{'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

#identical items in set

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))
'''
Returns a new set with all items from both sets by removing duplicates
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.union(set2))


set1.difference_update(set2)
print(set1)

'''
Return a set of all elements in either A or B, but not both
'''

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.symmetric_difference(set2))