from decimal import Decimal
from fractions import Fraction

#Create and Compare Numbers of Different Types

num_int = 5
num_float = 1.4
num_decimal = Decimal(1.7)
num_fraction_1 = Fraction(1,4)
num_fraction_2 = Fraction(2,4)

#Compare an integer and a float
print(num_int == num_float)
print(num_int != num_float)
print(num_int > num_float)
print(num_int < num_float)

#Compare decimal and float
print(num_decimal == num_float)
print(num_decimal != num_float)
print(num_decimal < num_float)
print(num_decimal > num_float)

#Compare two fractions
print(num_fraction_2 == num_fraction_1)
print(num_fraction_2 != num_fraction_1)
print(num_fraction_2 < num_fraction_1)
print(num_fraction_2 > num_fraction_1)
