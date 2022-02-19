'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input
'''

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        print('i : ',i)
        if string[i:].startswith(sub_string):
            print('inside i : ',string[i:])
            count += 1
    return count

def count_substring(string,sub_string):
    print(sum([ 1 for i in range(len(string)-len(sub_string)+1) if string[i:i+len(sub_string)] == sub_string]))


count_substring('abcdcdc', 'cdc')