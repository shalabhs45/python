str = 'My Name is Jessa'

words = str.split()

str1 = [word[::-1] for word in words]

print(" ".join(str1))

#yM emaN si asseJ


# Remove items from a list while iterating

# Expected Output - [10, 20, 30, 40, 50]

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(number_list)-1, -1, -1):
    if number_list[i] > 50:
        del number_list[i]
print(number_list)

num_list = list(filter(lambda n: n <50, number_list))
print (num_list)


#Reverse Dictionary mapping

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
# Reverse mapping
new_dict = {value: key for key, value in ascii_dict.items()}
print(new_dict)

