#Basic Arithmetic and Comparison Operators

#Write a program to check if a number is even or odd.
print("Please enter the number")
num_1 = int(input())

if num_1 % 2 == 0:
	print(f"{num_1} is even")
else:
	print(f"{num_1} is odd")

#Compare the values of a float and an int and print whether they are equal or not.

num_2 = float(num_1)

print(num_1 == num_2)

#Calculate the square of an integer and a float using the exponentiation operator (**).

square_num_1 = num_1**2
square_num_2 = num_2**2
print(square_num_1)
print(square_num_2)

#Write a program to find the maximum of three numbers using nested conditional operators.

ls = [10,11,7]

if ls[0] > ls[1]:
	if ls[0] > ls[2]:
		print(f"Max number is {ls[0]}")
	else:
		print(f"Max number is {ls[2]}")
else:
	if ls[1] > ls[2]:
		print(f"Max number is {ls[1]}")
	else:
		print(f"Max number is {ls[2]}")

#Accept two integer inputs from the user and calculate the absolute difference between them using the abs() function. Print the result.
print("Please enter two number for abs difference")
num_1_abs = int(input())
num_2_abs = int(input())

num_1_abs = abs(num_1_abs)
num_2_abs = abs(num_2_abs)
diff = num_1_abs - num_2_abs
print(diff)

#Accept an integer input from the user and use conditional statements to print whether the number is positive, negative, or zero.

num_1 = int(input())

if num_1 > 0:
	print("Postitive")
elif num_1 < 0:
	print("Negative")
else:
	print("Zero")

#Accept two integer inputs from the user. Check if the first number is a multiple of the second and print True if it is, otherwise print False.

print("Please enter two integer numbers")
num_1 = int(input())
num_2 = int(input())

if num_1 and num_2 % num_1:
	print(True)
else:
	print(False)
