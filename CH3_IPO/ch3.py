# print("It's working!")
# BOOLEANS

age = 20
minimum_age = 18

# print(age >= minimum_age)
# print(age <= minimum_age)

# has_ticket = True
# appropriate_age = age >= minimum_age
# let_them_in1 = has_ticket and appropriate_age
# print("has ticket and appropriate age: ", let_them_in1)

# age = 15
# has_ticket = True
# appropriate_age = age >= minimum_age
# let_them_in2 = has_ticket and appropriate_age
# print("has ticket and appropriate age: ", let_them_in2)

# age = 40
# has_ticket = False
# appropriate_age = age >= minimum_age
# let_them_in3 = has_ticket and appropriate_age
# print("has ticket and appropriate age: ", let_them_in3)

dan_score = 90
matthew_score = 100

print(f"Dan scored: {dan_score} | Matthew scored: {matthew_score}")

if dan_score > matthew_score:
    print("Dan scored higher than Matthew")
elif dan_score < matthew_score:
    print("Dan scored less than Matthew")
else:
    print("Dan and Matthew tied")

answer = input("Enter 'Yes' or 'No'")

clean_answer = answer.capitalize()
if clean_answer == "Yes":
    print("hello")
elif clean_answer == "No":
    print("Goodbye")
else: print("You didnt answer 'yes' or 'no'. Why?")