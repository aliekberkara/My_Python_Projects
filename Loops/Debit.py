print("""
******************************
Welcome to our ATM...

Operations:

1. Balance Inquiry

2. Depositing Money

3. Withdrawing Money

Type 'quit' to exit the program.
******************************

""")

balance = 10000

while True:
    operation = input("Enter A Operation: ")
    if operation == "1":
        print("Your Balance:", balance, "TL")
    elif operation == "2":
        amount = int(input("Enter The Amount Of Money You Want To Deposit: "))
        balance += amount
        print(amount, " TL Has Been Added To Your Balance.")
    elif operation == "3":
        amount = int(input("Enter The Amount Of Money You Want To Withdraw: "))
        balance -= amount
        print(amount, " TL Has Been Withdrawn From Your Balance.")
    elif operation == 'quit':
        print("We Wish You A Nice Day.")
        break
    else:
        print("Invalid Operation!")
