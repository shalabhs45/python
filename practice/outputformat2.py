'''
Type 3:  Display Output Number in Various Format

'''
number = 40

print("\n")
# 'd' is for integer number formatting
print("The number is:{:d}".format(number))

# 'o' is for octal number formatting, binary and hexadecimal format
print('Output number in octal format : {0:o}'.format(number))

# 'b' is for binary number formatting
print('Output number in binary format: {0:b}'.format(number))

# 'x' is for hexadecimal format
print('Output number in hexadecimal format: {0:x}'.format(number))

# 'X' is for hexadecimal format
print('Output number in HEXADECIMAL: {0:X}'.format(number))


'''
Display Numbers as a float type

'''

number = 30.238

print("\n")
# 'f' is for float number arguments
print("Output Number in The float type :{:f}".format(number))

# padding for float numbers
print('padding for output float number{:5.2f}'.format(number))

# 'e' is for Exponent notation
print('Output Exponent notation{:e}'.format(number))

# 'E' is for Exponent notation in UPPER CASE
print('Output Exponent notation{:E}'.format(number))



'''
Type 2: Output Alignment by Specifying a Width

'''
text = "This is my code"

print("\n")
# left aligned
print('{:<25}'.format(text))  # Right aligned print('{:>25}'.format(text))
# centered
print('{:^25}'.format(text))


'''
Type 3 - Specify Sign while diplaying numbers
'''

positive_number = float(input("Enter Positive Number "))
negative_number = float(input("Enter Negative Number "))

print("\n")
# sign '+' is for both positive and negative number
print('{:+f}; {:+f}'.format(positive_number, negative_number))

# sign '-' is only for negative number
print('{:f}; {:-f}'.format(positive_number, negative_number))