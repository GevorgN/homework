"""
Write a program with a global variable x. Create a function that changes the value of x inside the function and prints both the global and local values.

modify_variable() 
print("Global x:", x)
"""

x = 10
def modify_variable():
	global x
	x+=1
	return x

modify_variable() 
print("Global x:", x)

"""
Write a function is_even that takes a number and returns True if the number is even and False otherwise.
print(is_even(4)) # True
print(is_even(5)) # False
"""

def is_even(y):
	if y % 2 == 0:
		return True
	else:
		return False

print(is_even(4)) # True
print(is_even(5)) # False

"""
Write a function find_max that takes two numbers and returns the larger of the two.
print(find_max(10, 20))  # Example call
"""

def find_max(num1, num2):
	if num1 > num2:
		return num1
	elif num1 < num2:
		return num2
	else:
		return num1

print(find_max(10, 20))

"""
Write a function calculate_discount that takes a price and a discount percentage and returns the discounted price.
print(calculate_discount(100, 20))  # 20% off on 100
"""

def calculate_discount(amount, percent):
	res = amount*percent/100
	return f'{res}% off on {amount}'


print(calculate_discount(100, 20))

"""
Write a function filter_positive that takes a list of numbers and returns a new list containing only the positive numbers.
print(filter_positive([-5, 3, -1, 2, 0]))  # Example call

"""

def filter_positive(list_of_nums):
	new_list = []
	for i in list_of_nums:
		if i >= 0:
			new_list.append(i)
	return new_list

print(filter_positive([-5, 3, -1, 2, 0]))

"""
Write a function count_digits that takes an integer and returns the number of digits in it.
print(count_digits(12345))  # Example call
"""

def count_digits(num:int) -> int:
	num = int(num)
	count = 0
	while num > 1:
		num = num/10
		count+=1
	return count


print(count_digits(12345))

"""
Write a function sum_of_digits that calculates the sum of all digits in an integer
print(sum_of_digits(123))  # Example call
"""

def sum_of_digits(num:int):
	num = str(num)
	res = 0
	for i in num:
		res += int(i)
	return res 


print(sum_of_digits(123))