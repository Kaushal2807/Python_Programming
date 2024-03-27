# Problem: Create a function that returns both the area and circumference of a circle given its radius.

r = int(input("Enter a radius of circle:"))

def area(r):
    return 3.14*(r**2)

def circumference(r):
    return (2*3.14*r)

print("Area of circle is:",area(r))
print("Circumference of circle is:",circumference(r))