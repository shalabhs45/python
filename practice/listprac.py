aLsit = [100, 200, 300, 400, 500]

print(" Reverse: ",aLsit[::-1])

'''
Concatenate three Strings
'''
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = [i+j for i,j  in zip(list1, list2)]

print("List 3: ",list3)

aList = [1, 2, 3, 4, 5, 6, 7]

aList = [x *x for x in aList]

print(" Squares ", aList)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

resList = [x+y for x in list1 for y in list2]
print(resList)

'''
Exercise 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
'''
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)


'''
Exercise 6: Remove empty strings from the list of strings

'''
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
resList = list(filter(None, list1))
print(resList)