#Write a program that slices the first 3 characters and the last 2 characters from a string.

print("Please enter the string!")
str_1 = str(input())
print(str_1[2:-2])
print(f'Extracted characters are "{str_1[0:3]}" and "{str_1[-2:]}"')
