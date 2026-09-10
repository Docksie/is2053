#Write a program that asks the user for the number of miles driven and the gallons of gas used.

miles_driven = int(input("Enter the miles driven: "))
gallons_used = float(input("Enter the gallons of fuel used: "))

mpg = miles_driven / gallons_used
print(f"\nYour Miles Per Gallon is {mpg:.1f}.")