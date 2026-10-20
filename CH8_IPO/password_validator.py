# Input from the user.
# check whether it has an upper case letter or a lower case letter
# and a digit
# and is a min length

MINIMUM_PASSWORD_LENGTH = 7

def password_is_valid(password: str) -> bool:
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
    correct_length = len(password) >= MINIMUM_PASSWORD_LENGTH

    is_valid = has_upper and has_lower and has_digit and correct_length
    return is_valid

def display_pwd_requirements():
    print('=' * 30)
    print("Requirements: ")
    print(f"Min length: {MINIMUM_PASSWORD_LENGTH}")
    print("- At least 1 caps")
    print("- At least 1 lower")
    print("- At least 1 digit")
def main():
    display_pwd_requirements()
    password = input("Password: ")
    while not password_is_valid(password):
        print("Error: password not valid")
        password = input("Password: ")
    print("Welcome user!")



if __name__ == "__main__":
    main()