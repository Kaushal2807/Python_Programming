# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = int(input("Enter Your Score :- "))

if score >= 101:
    print("Score is invalid")

elif score >= 90:
    print("Your grade is : A")

elif score >= 80:
    print(" Your grade is : B")

elif score >= 70:
    print("Your grade is : C")

elif score >= 60 :
    print("Your grade is : D")

else:
    print("Your grade is : F")
