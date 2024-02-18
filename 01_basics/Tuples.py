tea_types = ("Masala", "Ginger", "Green")
print(tea_types)

print(tea_types[0])
print(tea_types[-1])
print(tea_types[1:])

print(len(tea_types))

more_tea=("Herbal","Earl Grey")
all_tea = more_tea+tea_types
print(all_tea)

if "Masala" in tea_types:
    print("Masala is there")

more_tea = ("Herbal", "Earl Grey","Herbal")
print(more_tea)

print(more_tea.count("Herbal"))

print(tea_types)

(black,green,Oolong) = tea_types 
print(black)
print(green)    
print(Oolong)

print(type(tea_types))