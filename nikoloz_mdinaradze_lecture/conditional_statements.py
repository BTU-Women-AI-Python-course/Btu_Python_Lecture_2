# Write a program that asks for the total amount of a purchase.
# If the amount is over $100, apply a 10% discount.
# If the amount is between $50 and $100, apply a 5% discount.
# If the amount is under $50, no discount is applied.
# Print the final amount after applying the discount.


total_amount = float(input("total amount: $"))
if total_amount <= 0:
    print("Invalid price")
else:
    if total_amount > 100:
        total_amount *= 0.9

    elif 50 <= total_amount <= 100:
        total_amount *= 0.95

    print(f"Discounted our price is {total_amount}$")
