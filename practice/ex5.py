while True:
    num = int(input("Enter a number between 1 - 100: "))
    if num > 100 or num < 0:
        print("Out of range, try again")
        continue
    elif num == 0:
        print("Goodbye")
        break
    else:
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")