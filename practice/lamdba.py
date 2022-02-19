'''
Program for even number with a lambda function
'''
l = [10, 5, 12, 78, 6, 1, 7, 9]
even_nos = list(filter(lambda x: x % 2 == 0, l))
print("Even numbers are: ", even_nos)


'''
Example: lambda function with  filter()
'''
l = [-10, 5, 12, -78, 6, -1, -7, 9]
positive_nos = list(filter(lambda x: x >0, l))

'''
map() function in Python
In Python, the map() function is used to apply some functionality for every element present in the given sequence and generate a new series with a required modification.

Ex: for every element present in the sequence, perform cube operation and generate a new cube list.

Syntax of map() function:

map(function,sequence)
where,

function – function argument responsible for applied on each element of the sequence
sequence – Sequence argument can be anything like list, tuple, string
'''

list1 = [2,3,4,8,9]

list2 = list(map(lambda x: x*x*x, list1))

print("Cube values are:", list2)

'''
reduce() function in Python
In Python, the reduce() function is used to minimize sequence elements into a single value by applying the specified condition.

The reduce() function is present in the functools module; hence, we need to import it using the import statement before using it.

Syntax of reduce() function:

reduce(function, sequence)
'''
from functools import reduce
list1 = [20, 13, 4, 8, 9]
add = reduce(lambda x, y: x+y, list1)
print("Addition of all list elements is : ", add)

print(sum(list1))
