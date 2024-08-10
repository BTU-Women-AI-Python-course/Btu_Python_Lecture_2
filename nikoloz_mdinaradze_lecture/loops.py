# Write a discount calculator using a while loop

while True:
    user_input = input("total amount in dollars (press Q to quit): ")
    if user_input == "Q":
        break
    total_amount = float(user_input)
    if total_amount <= 0:
        print("Invalid price")
    else:
        if total_amount > 100:
            total_amount *= 0.9

        elif 50 <= total_amount <= 100:
            total_amount *= 0.95

        print(f"Discounted our price is {total_amount}$")

# Calculate the discounted prices for items


items = [
    {
        "name": "laptop",
        "price": 800
    },
    {
        "name": "ball",
        "price": 10
    },
    {
        "name": "car",
        "price": 8000
    }
]

for item in items:
    if item['price'] <= 0:
        print("Invalid price")
    else:
        if item['price'] > 100:
            item["price"] *= 0.9

        elif 50 <= item["price"] <= 100:
            item["price"] *= 0.95
    print(f"Discounted price for {item['name']} is {item['price']}")


# for loops and dicts

dict1 = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

for key in dict1:
    print(key, dict1[key])

for key, value in dict1.items():
    print(key, value)
    