person = {"name": "Jessa", "country": "USA", "telephone": 1178}

# Get all keys
print(person.keys())
# output dict_keys(['name', 'country', 'telephone'])
print(type(person.keys()))
# Output class 'dict_keys'

# Get all values
print(person.values())
# output dict_values(['Jessa', 'USA', 1178])
print(type(person.values()))  
# Output class 'dict_values'

# Get all key-value pair
print(person.items())
# output dict_items([('name', 'Jessa'), ('country', 'USA'), ('telephone', 1178)])
print(type(person.items()))
# Output class 'dict_items'


# Iterating the dictionary using for-loop
print('key', ':', 'value')
for key in person:
    print(key, ':', person[key])

# using items() method
print('key', ':', 'value')
for key_value in person.items():
    # first is key, and second is value
    print(key_value[0], key_value[1])


    # count number of keys present in  a dictionary
print(len(person))  
# output 3

# update dictionary by adding 2 new keys
person["weight"] = 50
person.update({"height": 6})

# print the updated dictionary
print(person)
# output {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}

# set default value if key doesn't exists
person.setdefault('state', 'Texas')

# key doesn't exists and value not mentioned. default None
person.setdefault("zip")

# key exists and value mentioned. doesn't  change value
person.setdefault('country', 'Canada')

# Display dictionary
for key, value in person.items():
    print(key, ':', value)
