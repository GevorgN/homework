#String Basics and Slicing

#Create a program that extracts the first 5 characters from a given string.
str1 = input("Please input the string: ")
print(str1[0:5])

#Extract the last 3 characters of a string using slicing.
print(str1[-3::])

#Write a program to print every second character from a string.
print(str1[1::2])

#Reverse a given string using slicing and print the result.
print(str1[::-1])

#Replace all occurrences of a specific character with another character in a string.
str1 = "hello world"
print(str1.replace("l","L"))