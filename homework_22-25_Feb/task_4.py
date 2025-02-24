from fractions import Fraction
from decimal import Decimal


# Create Complex Numbers and Calculate Magnitude

num1_complex = complex(1,5)
num2_complex = 4+5j
magnidute_1 = (num1_complex.real**2 + num1_complex.imag**2)**0.5
print(magnidute_1)
magnidute_2 = (num2_complex.real**2 + num2_complex.imag**2)**0.5
print(magnidute_2)

"""
Create two fractions and perform addition, subtraction, multiplication, and division manually. Afterward, check the results using Python.
"""

num1_fraction = Fraction(5,4)
num2_fraction = Fraction(4,7)

sum_fraction = num1_fraction + num2_fraction
sub_fraction = num1_fraction - num2_fraction
mult_fraction = num1_fraction * num2_fraction
div_fraction = num1_fraction / num2_fraction

print(sum_fraction)
print(sub_fraction)
print(mult_fraction)
print(div_fraction)

#Create a decimal number and experiment with adding or subtracting very small decimal values.

num1_decimal = Decimal(7.4)

sum_decimal_1 = num1_decimal + Decimal(0.0001478)
sub_decimal_1 = num1_decimal - Decimal(0.0000047478)
sub_decimal_2 = num1_decimal - Decimal(0.0000000018)
sum_decimal_2 = num1_decimal + Decimal(0.000000000001578)

print(sum_decimal_1)
print(sum_decimal_2)
print(sub_decimal_1)
print(sub_decimal_2)
