#String Formatting and Simple Manipulations

#Write a program to print a formatted message like: "Hello, my name is James and I am 20 years old." using f-strings.
name = input("Please enter the name: ")
age = int(input("Please enter the age: "))

print(f"Hello, my name is {name} and I am {age} years old.")

#Create a program to format and print a float with 2 decimal places.
num = 1.2234
print(f"float with 2 decimal places : {num:.2f}")

#Write a program to convert all characters in a string to uppercase and then to lowercase.

str1 = "Hello World"
print(str1.lower())
print(str1.upper())

#Create a program to count the number of occurrences of a specific character in a string.

input_str = input("Enter the string: ")
input_specific_char = input("Enter specific character: ")

print(input_str.count(input_specific_char))

#Write a program to concatenate two strings with a space in between.
str1 = "hello"
str2 = "World"
my_tuple = ("hello", "World")

print(" ".join(my_tuple))
print(f"{str1} {str2}")

#Create a program to find the sum of the first and last digit of a given number.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

num1 = str(num1)[0]
num2 = str(num2)[-1]
sum_of_nums = int(num1) + int(num2)
print(sum_of_nums)


#Write a program to calculate the average of 3 float numbers and format the result to 3 decimal places.

fnum1 = 7.54561
fnum2 = 4.36467
fnum3 = 1.124667

average_num = (fnum1 + fnum2 + fnum3)/3
print(f"{average_num:.3f}")

#Create a program that takes a string input and an integer input and repeats the string that many times.

input_str = input("Enter string: ")
input_num = int(input("Enter integer: "))

print(input_str*input_num)

#Ask the user to enter a string, and then print the string in reverse order.

input_str = input("Enter the string: ")
print(input_str[::-1])

#Count how many vowels are in the string and print the count.

vowels = "aeiouAEIOU"
str1 = input("Enter the string: ")
count = 0

for i in str1:
	if i in vowels:
		count += 1

print(count)

#Write a program that takes a string as input and outputs the longest substring without repeating characters.
#For example, the string "abcabcbb" should return "abc".

str1 = input("Enter the string: ")
substring = ""

for i in str1:
	if i not in substring:
		substring += i

print(substring)


#Write a program using a while loop that repeatedly asks the user to input a number until they input 0, then print the sum of all entered numbers.
flag = 1
ls = []
while flag:
	input_num = int(input("Enter the number: "))
	if input_num == 0:
		flag = 0
	else:
		ls.append(input_num)
print(sum(ls))

#Create a list of 10 numbers (hardcoded) and calculate the sum of all numbers in the list.

ls = [1,2,3,4,5,6,7,8,9,10]
print(sum(ls))

#Հայտարարել list, և տպել list-ի էլեմենտներից առավելագույնի արժեքը: List-ը պետք է պարունակի միայն int տիպի արժեքներ: Չօգտագործել max ֆունկցիան:

ls = [1,27,32,44,50,67,71,18,29,10]

max_num = ls[0]
for i in ls:
	if max_num < i:
		max_num = i
print(max_num)

#Հայտարարել list և տպել նվազագույն արժեքով էլեմենտի ինդեքսը։

ls = [11,27,32,44,50,67,71,18,29,1]

min_num = ls[0]
min_num_index = 0
for i in range(len(ls)):
	if min_num > ls[i]:
		min_num = ls[i]
		min_num_index = i

print(min_num_index)

#Հայտարարել  երկու ամբողջ թվային արժեքներով list- եր  և տպել համապատասխանող ինդեքսներով էլեմնետների արտադրյալը էկրանին:

ls1 = [11,27,32]
ls2 = [0,1,2]

for i in range(len(ls1)):
	print(ls1[i]*ls2[i])

#Գրել ծրագիր, որը ստանում է ամբողջ թիվ։ Հայտարարել list: Եթե list-ում առկա է տրված թիվը տպել YES, հակառակ դեպքում տպել NO։ 

input_num = int(input("Enter the number: "))

input_list = list(input("Enter the elements: ").split())
flag = "NO"
for i in input_list:
	if input_num == int(i):
		flag = "YES"

print(flag)

#Հայտարարել list,  որը բաղկացած է string-ներից: Տպել թե քանի անգամ է յուրաքանչյուրը հանդիպում list-ում: 

input_list = list(input("Enter the elements: ").split())

for i in set(input_list):
	print(f"{i} - {input_list.count(i)}")