tea_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green":"Mild"}
print(tea_types)

print(tea_types["Masala"])

print(tea_types.get("Ginger"))

print(tea_types)

tea_types["Green"] = "Fresh"
print(tea_types)

for variable in tea_types:
    print(variable)

for keys in tea_types:
    print(keys,tea_types[keys])

for key ,value in tea_types.items():
    print(key,value)

if "Masala" in tea_types:
    print("Masala tea is present")

print(len(tea_types))

print(tea_types)
tea_types["Earl Grey"] = "Strong"
print(tea_types)

tea_types.pop("Green")
print(tea_types)

tea_types.popitem()
print(tea_types)

del tea_types["Ginger"]
print(tea_types)

tea_types_copy = tea_types.copy()
print(tea_types_copy)

tea_shop={
    "Tea":{"Masala": "Spicy", "Ginger": "Zesty", "Green":"Mild"},
    "Coffee":{"Black": "Strong", "Latte": "Mild", "Cappuccino":"Mild"}
}

print(tea_shop)

print(tea_shop["Tea"])
print(tea_shop["Tea"]["Masala"])

squared_nums = {x: x**2 for x in range(10)}
print(squared_nums)

keys = ["Masala", "Ginger", "Green"]
print(keys)

default_values = "Mild"
print(default_values)

new_tea_types = dict.fromkeys(keys,default_values)
print(new_tea_types)
