# Problem: Compute the factorial of a number using a while loop.

num = int(input("Enter a number :- "))
number = num
factorial = 1 

while number > 0:
    factorial = factorial * number
    number = number - 1 
print(f"Factorial of {num} is :- ",factorial)

