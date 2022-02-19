from sys import argv

print("Total argument passed: ", len(argv))

'''
Output Formatting


Type 1

'''
print('FirstName - {0}, LastName - {1}'.format('Ault', 'Kelly'))


'''
Type2

'''

firstName = input("Enter First Name ")
lastName = input("Enter Last Name ")
organization = input("Enter Organization Name ")

print("\n")
print('{0}, {1} works at {2}'.format(firstName, lastName, organization))
print('{1}, {0} works at {2}'.format(firstName, lastName, organization))
print('FirstName {0}, LastName {1} works at {2}'.format(firstName, lastName, organization))
print('{0}, {1} {0}, {1} works at {2}'.format(firstName, lastName, organization))


'''
Type 3 Accessing Output String Arguments by name

'''
name = input("Enter Name ")
marks = input("Enter marks ")

print("\n")
print('Student: Name:  {firstName}, Marks: {percentage}%'.format(firstName=name, percentage=marks))
