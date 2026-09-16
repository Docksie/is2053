# This program asks the user to enter a series of positive numbers and displays the min, max, average, and total values

value = 1.0
total = 0.0
count = 0
min_num = 0.0
max_num = 0.0

value = float(input(f"Enter a positive number to add and negative number to quit - Number {int(count + 1):02}: "))

while value > 0:
    total += value
    if min_num == 0: min_num = value
    elif min_num > value: min_num = value
    if max_num < value: max_num = value
    count += 1
    value = float(input(f"Enter a positive number to add and negative number to quit - Number {int(count + 1):02}: "))


avg_num = total / count

print(f"\nThe minimum of all {count} numbers is {min_num:.1f}")
print(f"The maximum of all {count} numbers is {max_num:.1f}")
print(f"The average of all {count} numbers is {avg_num:.1f}")
print(f"The total of all {count} numbers is {total:.1f}")


    