
def min_value(num_one: int, num_two: int, num_three: int) -> int:
    if num_one < num_two and num_one < num_three:
        return num_one
    elif num_two < num_one and num_two < num_three:
        return num_two
    else:
        return num_three

def max_value(num_one: int, num_two: int, num_three: int) -> int:
    if num_one > num_two and num_one > num_three:
        return num_one
    elif num_two > num_one and num_two > num_three:
        return num_two
    else:
        return num_three

def same_value(num_one: int, num_two: int, num_three: int) -> bool:
    if num_one == num_two == num_three:
        return True
    else:
        return False




def main() -> None:
    num_one = int(input("Enter number 1: "))
    num_two = int(input("Enter number 2: "))
    num_three = int(input("Enter number 3: "))

    if same_value(num_one, num_two, num_three):
        print("\nAll numbers are the same")
    else:
        print(f"\nThe minimum number is: {min_value(num_one, num_two, num_three):.1f}")
        print(f"The maximum number is: {max_value(num_one, num_two, num_three):.1f}")
        print(f"The average of the numbers is: {((num_one + num_two + num_three) / 3):.1f}")
        print(f"The total of the numbers is: {(num_one + num_two + num_three):.1f}")

if __name__ == "__main__":
    main()
