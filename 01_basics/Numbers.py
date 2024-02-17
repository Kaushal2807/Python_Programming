x = 2
y = 3
z = 4

print(x+y)   # Addition

print(x**y)  # Power of

print((x + y) * z)  # BODMAS or precedence 

print(40+2.23) # Addition of int and float

print(int(40+2.23))  # Type casting for float to int

print(float(40))  # Type casting for int to float

print('Hello ' + 'World')  # Concatenation

print(x,y,z) # Multiple print statements

print(type(x))  # Type of x

print(x+1)  # Increment

print(y*2)  # Multiplication

print(y % 2) # Modulus

print(100 ** 2)  # Power of

print(2 ** 1000)  # Power of

result = 1/3.0
print(result)  # Division

print(repr('Hello'))
print(str('Hello'))
print('Hello')

# Comparison

print(1 < 2)

print(5.0 == 5.0)

print(4.0 != 5.0)

print(x < y < z)

print(x < y and y < z) # Logical AND x < y ==> true and y < z ==> true

print(x < y or y < z) # Logical OR x < y ==> true or y < z ==> true

print(1 == 2 < 3) 

print(1 == 2 and 2 < 3) # Logical AND 1 == 2 ==> false and 2 < 3 ==> true

print(1 == 2 or 2 < 3) # Logical OR 1 == 2 ==> false or 2 < 3 ==> true


import math 

a = math.floor(2.3) # Floor function positive number will decrease the value and negative number will increase the value
print(a)
a = math.floor(-4.5) 
print(a)
a = math.floor(3.9)
print(a)
a = math.floor(-3.4)
print(a)
a = math.floor(-9.9)
print(a)
a = math.floor(-9.1)
print(a)
a = math.floor(3.2)
print(a)

# trunc mobe towards zero 

b = math.trunc(2.8)
print(b) 
b = math.trunc(-3.9)
print(b)


print (999999999999999999999 + 1) #python number percesion
print (999999999999999999999 * 2.1) 

print(2+1j) # Complex number
print((1 + 1j) * 3) # Complex number

print(0o20) # Octal number
print(0x20) # Hexadecimal number
print(0xFF) # Hexadecimal number
print(0b10) # Binary number

print(oct(64)) # Octal number
print(oct(16)) # Octal number
print(hex(64)) # Hexadecimal number
print(bin(64)) # binary number

print(int('64',8)) # Octal number
print(int('64',16)) # Hexadecimal number
print(int('10000',2)) # binary number

x = 1
y = x << 2 # Left shift
print(y)

y = x >> 2 # Right shift
print(y)

import random
print(random.random()) # Random number between 0 and 1
print(random.randint(1,10)) # Random number between 1 and 10 (int value)

li =['Lemon','Masala','Tea']
print(random.choice(li)) # Random choice from list
random.shuffle(li) # Random shuffle from list
# print(li)

print(0.1+0.1+0.4)
print(0.1+0.1+0.1)
print(0.1+0.1+0.1-0.3)
print((0.1+0.1+0.1)-0.3)

from decimal import Decimal # For Decimal number
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))

from fractions import Fraction # For Fraction number 
myfraction = Fraction(3,4)
print(myfraction)