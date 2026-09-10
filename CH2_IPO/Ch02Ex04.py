# Python Ch02Ex04.py

# This program calculates total amount of meal purchased at a restaurant.

# tip percent is 18
TIP = 0.18
# sales tax percent is 7
SALES_TAX = 0.07
#ask user to enter the charge for the food

food_charge = float(input("Enter the charge for food: "))

print(f"\nThe Tip ({TIP:.0%}) on the food charge of ${food_charge:.2f} is ${food_charge * TIP:.2f}")
print(f"The Tax ({SALES_TAX:.0%}) on the food charge of ${food_charge:.2f} is ${food_charge * SALES_TAX:.2f}")
print(f"The Total amount, including Tax and Tip, is ${food_charge + (food_charge * TIP) + (food_charge * SALES_TAX):.2f}")