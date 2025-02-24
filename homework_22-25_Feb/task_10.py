#Write a program that takes a string and converts it to both uppercase and lowercase.

print("Please enter the first string")
str_1 = str(input())
print("Please enter the second string")
str_2 = str(input())
full_string = str_1 + " " + str_2
upper_string = full_string.upper()
lower_string = full_string.lower()
print(F"'{upper_string}' and '{lower_string}'")



