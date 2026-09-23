# this program determines a movie ticket price based on age and whether it's a matinee showing

age = int(input("Enter your age: "))

if age < 13:
    print("$8")
elif age <= 64:
    is_matinee = input("Is it a matinee? (yes/no): ")
    if is_matinee.lower() == "yes":
        print("$9")
    else:
        print("$12")
else:
    print("$10")
