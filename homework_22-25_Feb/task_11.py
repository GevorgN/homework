#Write a program that checks whether a string starts with the letter "A" and ends with the letter "Z".

print("Please enter the string")
str_1 = str(input())
A = False
Z = False

if str_1[0] == "A":
    A = True
if str_1[-1] == "Z":
    Z = True

print(f"Starts with 'A': {A}, Ends with 'Z': {Z}")
