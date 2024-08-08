clients = [
  {
    "name": "mariami",
    "age": 20,
    "salary": 7000,
    "loan_amount": 50000,
    "year": 7
  },
  {
    "name": "ana",
    "age": 50,
    "salary": 2500,
    "loan_amount": 100000,
    "year": 5
  },
  {
    "name": "anano",
    "age": 13,
    "salary": 0,
    "loan_amount": 5000,
    "year": 2
  }
]

for client in clients:
    if client['age'] >= 18:
        monthly_amount = ((client["loan_amount"] * 1 / 5) *
                          client["year"] + client["loan_amount"]) / (client["year"] * 12)
        if monthly_amount > (client["salary"] / 2):
            print(f"{client['name']}, You do not have enough money!")
        else:
            print(f"{client['name']}, You have enough money!")
    else:
        print(f"{client['name']}, You are not allowed to pay this year.")
