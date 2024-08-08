age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))  # in lari
loan_amount = int(input("Enter your loan amount: "))  # in lari
year = int(input("Enter your year: "))

if age >= 18:
    monthly_amount = ((loan_amount * 1 / 5) * year + loan_amount) / (year * 12)
    if monthly_amount > (salary / 2):
        print("You are not enough money!")
    else:
        print("You are enough money!")
else:
    print("You are not allowed to pay this year.")
