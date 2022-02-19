for char in range ('a','z'):
    print(char)
# range from 'a' to 'z
def character_range(char1, char2):
    for char in range(ord(char1), ord(char2) + 1):
        yield (char)
print("")

for letter in character_range('a', 'z'):
    print(chr(letter), end=', ')

# slicing
for i in range(10)[3:8]:
    print(i, end=' ')
# output 3 4 5 6 7
print('')
for i in reversed(range(10, 21)):
    print(i, end=' ')
# Output 20 19 18 17 16 15 14 13 12 11 10
print('')
'''
Use range() to reverse a list

'''

list1 = [10, 20, 30, 40, 50]
# start = list's size
# stop = -1
# step = -1

# reverse a list
for i in range(len(list1) - 1, -1, -1):
    print(list1[i], end=" ")
# Output 50 40 30 20 10

# negative indexing
# access last number
print(range(10)[-1])
# Output 9

# access second last number
print(range(10)[-2])
# Output 8