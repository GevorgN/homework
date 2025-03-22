#Write a function named greet that prints "Hello, World!". Call the function. 

def hello_world():
	print("Hello World!")

hello_world()

#Write a function add that takes two numbers as arguments and returns their sum. Call the function with different inputs.

def add(x:int,y:int)->int:
	summ = int(x) + int(y)
	return summ

print(add(7,'7'))
print(add(1,6))
print(add(5,4))


#Create a function multiply that takes two numbers and returns their product.

def mult(x:int,y:int)->int:
	sum_mult = int(x) * int(y)
	return sum_mult

print(mult(7,'7'))
print(mult(1,6))
print(mult(5,4))


#Write a function personal_greet that takes a name as an argument and prints "Hello, [name]!".

def greeting(name:str) -> str:
	print(f"Hello, {name}")

greeting('John')

"""
Write a function calculate_area that takes length and width as parameters and returns the area of a rectangle.
print(calculate_area(5, 10))  # Example call
"""

def calculate_area(x:int, y:int) -> int:
	area = int(x) * int(y)
	return area

print(calculate_area(5, 10)) 

"""
Write a function greet_with_message that takes a name and an optional message. The default message should be "Welcome!".

greet_with_message("Alice") # Default message greet_with_message("Bob", "Good morning!") # Custom message
"""

def greet_with_message(name:str, message = 'Good morning!') -> str:
	str_greet = f'{name}, {message}'
	return print(str_greet)


greet_with_message("Bob", "Good morning!")
greet_with_message("Alice")


"""
Write a function power that takes a number and an optional exponent. The default exponent should be 2 (square the number).
print(power(3)) # 3^2 
print(power(3, 3)) # 3^3
"""

def power(x:int, y=2) -> int:
	res = int(x)**int(y)
	return res

print(power(3)) # 3^2 
print(power(3, 3)) # 3^3