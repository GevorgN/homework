#Write a program that takes a string and extracts the first and last character using subscripts (indexing).

print("Please enter the string!")
str_1 = str(input())
print(str_1[1:-1])
print(f"Extracted charachters are '{str_1[0]}' and '{str_1[-1]}'")
