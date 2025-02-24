import random

#Create two integer variables and perform addition, subtraction, multiplication, and division.

first_number_int = random.randint(1, 1000)
second_number_int = random.randint(1, 1000)

sum_int = first_number_int + second_number_int
print(f'Sum of two int numbers - {sum_int}')

sub_int = first_number_int - second_number_int
print(f'Sub of two int numbers - {sub_int}')

div_int = first_number_int / second_number_int
div_int = round(div_int)
print(f'Div of two int numbers - {div_int}')

mult_int = first_number_int * second_number_int
print(f'Mult of two int numbers - {mult_int}')

#Repeat the same for two floating-point numbers.

first_number_float = random.uniform(1.1, 999.9)
second_number_float = random.uniform(1.1, 999.9)

sum_float = first_number_float + second_number_float
print(f'Sum of two float numbers - {sum_float}')

sub_float = first_number_float - second_number_float
print(f'Sub of two float numbers - {sub_float}')

div_float = first_number_float / second_number_float
print(f'Div of two float numbers - {div_float}')

mult_float = first_number_float * second_number_float
print(f'Mult of two float numbers - {mult_float}')

#Repeat the same for complex numbers.

first_number_int = random.randint(1, 1000)
second_number_int = random.randint(1, 1000)
third_number_int = random.randint(1, 1000)
forth_number_int = random.randint(1, 1000)


first_number_complex = complex(first_number_int, second_number_int)
second_number_complex = complex(third_number_int, forth_number_int)

sum_complex = first_number_complex + second_number_complex
print(f'Sum of two complex numbers - {sum_complex}')

sub_complex = first_number_complex - second_number_complex
print(f'Sub of two complex numbers - {sub_complex}')

div_complex = first_number_complex / second_number_complex
print(f'Div of two complex numbers - {div_complex}')

mult_complex = first_number_complex * second_number_complex
print(f'Mult of two complex numbers - {mult_complex}')
