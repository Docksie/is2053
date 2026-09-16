# This program calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, two pennies the second day, and continues to double each day.

num_days = int(input("Enter the number of days: "))
pay_count = 0.01
balance = 0.0
DAY_WIDTH = 7
PAY_WIDTH = 14
BALANCE_WIDTH = 23
break_line = "--------------------------------------------"


print("\nDay:\tPay\t\tBalance")
print(break_line)
for day in range(1, num_days + 1):
    balance += pay_count
    print(f"{day:<10}${pay_count:<10,.2f}${balance:<10,.2f}")
    pay_count *= 2
print(break_line)
print(f"The total salary for {num_days} days is: ${balance:,.2f}")
