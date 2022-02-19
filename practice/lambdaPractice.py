


#print((lambda x: x + 1)(2))

full_namer= lambda  first, last: f'Full Name: {first} {last}'


test= lambda x: (x % 2 and 'odd' or 'even')

#print(test(3))



ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']


sorted_ids = sorted(ids, key = lambda x: int(x[2:]))  # Sort per integers

#print(sorted_ids)


list = list(map(lambda x: x.capitalize(), ['cat', 'dog']))
print(list)