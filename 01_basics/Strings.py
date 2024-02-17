hello = "Hello, World!"
print(hello)

first_char = hello[0]
print(first_char)

slice_hello = hello[0:5]
print(slice_hello)

print(hello[-1]) #Negative indexing

num_list = "0123456789"
num_list_slice = num_list[3:]
print(num_list_slice)
num_list_slice = num_list[:7]
print(num_list_slice)
num_list_slice = num_list[0:7:2]
print(num_list_slice)
print(hello.capitalize())
print(hello.lower())
print(hello.upper())

hello = "   World    "
print(hello)
print(hello.strip())

hello = "Ginger"
print(hello.replace("Ginger","Lemon"))

hello = "Lemon, Ginger, Masala, Mint"
print(hello.split(", "))

hello = "Lemon masala "
print(hello.find("masala"))

hello = "Masala tea tea tea"
print(hello.count("tea"))

hello = "Masala"
quantity = 2 
order = "I ordered {} cups of {} chai"
print(order)
print(order.format(quantity,hello))

hello_v= ["Lemon", "Masala", "Ginger"]
print(hello_v)

print("_".join(hello_v))

hello = "Masala tea"
print(len(hello))

for letter in hello:
    print(letter)

world = "He said, \"Masala is awesome\""
print(world)

a = "Masala\ntea"
print(a)

a = r"Masala\ntea"
print(a)

b = r"c:\\user\\pwd\\"
print(b)

b = r"c:\user\pwd"
print(b)

hello = "world"
print("world" in hello )
print("World" in hello )