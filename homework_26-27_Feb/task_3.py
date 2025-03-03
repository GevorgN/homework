#Number Types

#Create a program that adds, subtracts, multiplies, and divides two integers, two floats, and a combination of both.

num_int_1 = int(input("Please enter first int number: "))
num_int_2 = int(input("Please enter second int number: "))
num_float_1 = float(input("Please enter first float number: "))
num_float_2 = float(input("Please enter second float number: "))

add_int = num_int_1 + num_int_2
sub_int = num_int_1 - num_int_2
mult_int = num_int_1 * num_int_2
div_int = num_int_1 / num_int_2

print(add_int, sub_int, mult_int, div_int)

add_float = num_float_1 + num_float_2
sub_float = num_float_1 - num_float_2
mult_float = num_float_1 * num_float_2
div_float = num_float_1 / num_float_2

print(add_float, sub_float, mult_float, div_float)

add_num = num_float_1 + num_int_2
sub_num = num_int_1 - num_float_2
mult_num = num_int_2 * num_float_2
div_num = num_float_1 / num_int_1

print(add_num, sub_num, mult_num, div_num)

#Write a program to calculate the product of two complex numbers.
num_complex_1 = 7 + 8j
num_complex_2 = 2 + 7j

num = num_complex_1 * num_complex_2

print(num)

#Create a fraction that represents 1/2 and another fraction representing 2/3. Add them and print the result.

import fractions

num_frac_1 = fractions.Fraction(1,2)
num_frac_2 = fractions.Fraction(2,3)

num_add_frac = num_frac_1 + num_frac_2
print(num_add_frac)

#Using decimal, calculate the sum of 0.1 and 0.2 and compare it with float.

from decimal import Decimal

num_1_deciaml = Decimal(0.1)
num_2_deciaml = Decimal(0.2)
sum_decimal = num_1_deciaml + num_2_deciaml

num_float = 0.3

print(sum_decimal == num_float)

#Write a program to check if the sum of three numbers is equal to 100. Use boolean comparisons to print the result as True or False.

print([True if sum(int(x) for x in input("Please input three number: ").split()) == 100 else False])

#Accept two fractions from the user (in the form of a/b where both a and b are integers) and multiply them. Use the fractions.Fraction class to handle fractions and print the resulting fraction in its simplified form.

num_frac_1 = fractions.Fraction(input("Please enter the first fraction number in this form a/b: "))
num_frac_2 = fractions.Fraction(input("Please enter the second fraction number in this form a/b: "))

sum_frac = num_frac_1 * num_frac_2

print(sum_frac)

#Accept two fractions from the user and find their GCD using the math.gcd() function along with the numerator and denominator attributes of each fraction.
import math

num_frac_1 = fractions.Fraction(input("Please enter the first fraction number in this form a/b: "))
num_frac_2 = fractions.Fraction(input("Please enter the second fraction number in this form a/b: "))

gcd_num_1 = math.gcd(num_frac_1.numerator,num_frac_2.numerator)
gcd_num_2 = math.gcd(num_frac_1.denominator,num_frac_2.denominator)

print(gcd_num_1, gcd_num_2)
