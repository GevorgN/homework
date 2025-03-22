#Write a function fibonacci(n) that calculates the nth Fibonacci number without using recursion.
#Use an iterative approach to compute the result.

def fibonacci(n):
	first = 0
	second = 1
	res = second
	if n == 0:
		return 0
	while n != 1:
		res = first + second
		first, second = second, res
		n -= 1
	return res

print(fibonacci(7))


#Write a function factorial(n) that calculates the factorial of a given number using an iterative approach. 

def factorial(n):
	sum_res = 1
	if n <= 1:
		return 1
	for i in range(1,n+1):
		sum_res *= i
	return sum_res

print(factorial(4))


#Write a function is_prime(n) that checks if a number is a prime number using a loop.
#The function should return True if the number is prime and False otherwise.

def is_prime(n):
	for i in range(2,n+1):
		if n%i!=0:
			return True
		return False

print(is_prime(3))

#Write a function reverse_string(s) that reverses a string without using slicing or built-in functions like reversed().
#Use a loop to construct the reversed string.

def reverse_string(s):
	new_str = ''
	if len(s) == 0:
		return None
	lenght = len(s)
	while lenght != 0:
		new_str += s[lenght-1]
		lenght -=1
	return print(new_str)


reverse_string('ab')

#Իրականացնել ֆունկցիա, որն ընդունում է թիվ և վերադարձնում նրա թվանշանների գումարը:

def sum_of_digits(n):
	res = 0
	if n == 0:
		return 0
	while n >= 1:
		res += n%10
		n //= 10 
	return res

print(sum_of_digits(123))

#Իրականացնել int տիպի արժեք վերադարձնող ֆունկցիա, որը վերադարձնում է՝ 1, 
#եթե ֆունկցային փոխանցված ամբողջ թիվը կարող է արտահայտվել երկու պարզ թվերի գումարով, հակառակ դեպքում ֆունկցիան կվերադարձնի՝ 0:

def sum_of_primes(num):
	def is_prime(n):
		for i in range(2,n+1):
			if n%i!=0:
				return True
			return False	

	if num < 4:
		return 0

	for i in range(2, num // 2 + 1):
		if is_prime(i) and is_prime(num - i):
			return 1

	return 0

print(sum_of_primes(5))
print(sum_of_primes(10))

#Իրականացնել ֆունկցիա, որը ունի հետևյալ նախատիպը (prototype)  def power (num: int, exp:int):
#Ֆունկցիան վերադարձնում է num ամբողջ թվի exp աստիճանի արժեքը։

def power(num: int, exp:int) -> int:
	if exp == 0:
		return 1
	res = num ** exp
	return res

print(power(2,5))

#Մուտքագրել թիվ, տպել թվի թվանշանները առանձին առանձին էկրանին։
#Օրինակ՝ մուտքագրված 5479 թվի համար տպել ‘5’, ‘4’, ‘7’, ‘9’։

def print_digit(n:int):
	new_ls = []
	while n >= 1:
		new_ls.append(str(n%10))
		n //=10

	print(*new_ls)


print_digit(5479)