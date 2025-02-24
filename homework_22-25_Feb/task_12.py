#Write a program that counts how many times the letter "a" appears in a given string.

print("Please enter the string")

str_1 = str(input())

count = 0
for i in str_1:
    if i == 'a':
        count += 1

print(f'"a" appears {count} times')
