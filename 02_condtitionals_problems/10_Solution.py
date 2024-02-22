# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

animal =input("Enter animal as Dog or Cat:-")

if animal =="Dog":
    year = int (input("Enter the age of Dog:-"))

    if year < 2 :
        print("Puppy Food")
    else:
        print("Senior dog food")
    

elif animal =="Cat":
    year = int (input("Enter the age of  Cat :- "))

    if year > 5:
        print("Senior cat food")
    else:
        print("Any light food")

else:
    print("Valid input is Dog or Cat")