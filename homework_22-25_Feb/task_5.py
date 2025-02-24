from decimal import Decimal
from fractions import Fraction

"""Create examples to compare two numbers using all relational operators 
(>, <,==, !=, >=, <=). Write down the results for different types of numbers."""

num_int = 15
num_float = 13.5
num_complex = 7 + 5j
num_decimal = Decimal(14.4)
num_fraction = Fraction(17,3)

res_1 = num_int > num_float
res_2 = num_fraction < num_decimal
res_3 = num_float == num_complex
res_4 = num_decimal != num_float
res_5 = num_int >= num_fraction
res_6 = num_decimal <= num_int

print(f'Result of ">" - {res_1}')
print(f'Result of "<" - {res_2}')
print(f'Result of "==" - {res_3}')
print(f'Result of "!=" - {res_4}')
print(f'Result of ">=" - {res_5}')
print(f'Result of "<=" - {res_6}')






