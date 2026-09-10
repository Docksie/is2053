## Write a program that displays the following:

# The distance the car will travel in 5 hours
speed = int(input("Enter the speed the car is traveling: "))
first_distance = 5 * speed
second_distance = 10 * speed
third_distance = 15 * speed

print("The car will travel the following distances:")
print(f"{first_distance:,} miles in 5 hours.")
print(f"{second_distance:,} miles in 10 hours.")
print(f"{third_distance:,} miles in 15 hours.")