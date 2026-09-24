# def three_prints():
#     print("Hello")
#     print("Welcome")
#     print("Goodbye")
#     print()

# three_prints()
# three_prints()
# three_prints()

# def get_ingredients():
#     print("Get the bread")
#     print("Get the jam")
#     print("Get the PB")
#     print()

# def make_sandwich():
#     print("Place 2 slices of bread on a plate")
#     print("more directions...")
#     print()

# def eat_sandwich():
#     print("nom nom")
#     print()

# def clean_up():
#     print("Put ingredients away")
#     print("Wash dishes")
#     print("Wipe surfaces")
#     print()

# get_ingredients()
# make_sandwich()
# eat_sandwich()
# clean_up()

# ----------------------------------------------------------
# PARAMETERS
# ------------------------------------------------------


# def greets_students(name:str = "Charlie"):
#     print(f"Hello {name}")

# greets_students()

# def show_students_grade(student:str, grade:float):
#     print(f"Hello, {student}. Your grade is {grade}")

# show_students_grade("Olivia", 55.5)

# --------------------------------------
# VALUE RETURNING FUNCTIONS
# --------------------------------------

# def half_square(number):
#     return number ** 2 / 2

# print(half_square(8))

# --------------------------------------
#   IMPORTS
# --------------------------------------

# import math

# print(math.sqrt(25))
# print(math.ceil(4.2))
# print(math.floor(4.2))
# print(math.pi)

# def get_name():
#     name = input("What is name?" )
#     return name

# def greet(name):
#     print(f"Hello, {name}")

# def main():
#     greet(get_name())

# main()

# ------------------------
# GLOBAL CONSTANTS
# ------------------------

#imports


# DEFINING CONSTANTS
SQUARE_FEET_PER_ACRE = 43560

# HELPER FUNCTIONS
def calc_tri_area(base, height):
    return base * height / 2

def convert_to_acres(sq_ft):
    return sq_ft / SQUARE_FEET_PER_ACRE

# MAIN FUNCTION

def main():
    front_area = calc_tri_area(300, 200)
    side_area = calc_tri_area(250, 150)
    back_area = calc_tri_area(400, 225)

    total_area = front_area + side_area + back_area

    total_area_in_acres = convert_to_acres(total_area)
    print(f"Total sqft: {total_area}\nTotal acres: {total_area_in_acres}")

if __name__ == "__main__":
    main()