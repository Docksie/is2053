# python print_formatting2.py

item_name = "wireless mouse"
price = 24.5
quantity = 3

subtotal = price * quantity
print(f"Item: {item_name}\nPrice: ${price:.2f}\nQuantity: {quantity}\nSubtotal: ${subtotal:.2f}")


#commas
large_number = 12321892738294
print(f"${large_number:,.2f}")

completion_rate = 0.875
print(f"Test completion: {completion_rate:.1%}")

print()
print()
# left justify
print(f"{item_name:<20}{quantity:<10}{price:<10}")
# right justify
print(f"{item_name:>20}{quantity:>10}{price:>10}")
# middle justify
print(f"{item_name:^20}{quantity:^10}{price:^10}")