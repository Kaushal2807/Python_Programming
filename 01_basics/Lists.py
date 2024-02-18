tea_varities = ["Masala", "Ginger", "Lemon", "Mint"]
print(tea_varities)

print(tea_varities[-1])
print(tea_varities[1:3])

tea_varities[0] = "Masala Chai"
print(tea_varities)

print(tea_varities[-1:-3:-1])

tea_varities[1:2] ="LEmon"  # 'L', 'E', 'm', 'o', 'n' it treated by array as individual elements
print(tea_varities)

tea_varities = ["Masala", "Ginger", "Lemon", "Mint"]
print(tea_varities)

print(tea_varities[1:2])

tea_varities[1:2] =["Black"]  # ['Lemon'] it treated by array as single element
print(tea_varities)

tea_varities[1:3] = ["White", "Green"]
print(tea_varities)

print(tea_varities[1:1])
tea_varities[1:1] = ["Yellow","Black"]
print(tea_varities)

print(tea_varities[1:3])

tea_varities = ["Masala", "Ginger", "Lemon", "Mint"]
for tea in tea_varities:
    print(tea)

for tea in tea_varities:
    # print(tea, end="-")
    pass

tea_varities.append("Oolong")
if "Oolong" in tea_varities:
    print("Oolong is there")

tea_varities.pop()
print(tea_varities)

tea_varities.remove("Ginger")
print(tea_varities)

tea_varities.insert(1,"Ginger")
print(tea_varities)

tea_varities.insert(4,"Oolong")
print(tea_varities)

tea_varities_copy = tea_varities.copy() 
print(tea_varities_copy)

tea_varities_copy.append("lemo00n")
print(tea_varities)
print(tea_varities_copy)

squared_nums=[x**2 for x in range(10)]
print(squared_nums)

cube_nums = [y**3 for y in range(5)]
print(cube_nums)
