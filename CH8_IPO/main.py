# python main.py

def describe_string(my_string:str):
    print('=' * 30)
    print(f"Original String: {my_string}")
    print(f"Alphanumeric: {my_string.isalnum()}")
    print(f"Alphabet only: {my_string.isalpha()}")
    print(f"Digits only: {my_string.isdigit()}")
    print(f"Lowercase: {my_string.islower()}")
    print(f"Uppercase: {my_string.isupper()}")
    print(f"Whitespace: {my_string.isspace()}")
    print(f"Capitalized: {my_string.istitle()}")

def main():
    dif_strings = [
        "Python"
    ]

    for my_str in dif_strings:
        describe_string(my_str)

    # # slicing
    # name = "Jordan Caleb Seigrist"
    # print(f"Full name: {name}")
    # print(f"First name: {name[:6]}")
    # print(f"Middle name: {name[7:12]}")
    # print(f"Last name: {name[13:21]}")
    # print(f"Last name: {name[-8:]}")
    # print(f"Reverse name: {name[::-1]}")



    # f_name = "Dordan"
    # l_name = "Seigrist"

    # # concatenation
    # full_name = f_name + ' ' + l_name
    # print(f"full name: {full_name}")

    # # crap i made a mistake

    # correct_spelling = "J" + full_name[1:]
    # print(correct_spelling)

    # # repetition operation -> *
    # full_name_10 = correct_spelling * 10
    # print(full_name_10)

    # print(f"The complete string: {name}")
    # print()

    # # iterate
    # print("Iterate over name")
    # for char in name:
    #     print(char)
    # print()

    # # Index
    # print(f"second character is {name[1]}")

    # # just like lists, we can use len and range together to index.

    # for _ in range(len(name)):
    #     print (f"Index: {_} | {name[_]}")

if __name__ == "__main__":
    main()