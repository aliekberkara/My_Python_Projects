"""
Problem 1

Try to find out if a number you get from the user is perfect.
A number is called a "perfect number" if the sum of its divisors is equal to itself.
For example, 6 is a perfect number. (1 + 2 + 3 = 6)
"""
while True:
    total = 0
    number = input("Enter A Number:(Type 'quit' to log out.) ")
    if number == 'quit':
        print("We Hope You Come Again...")
        break
    else:
        number = int(number)
        for i in range(1, (number // 2) + 1):
            if number % i == 0:
                total += i
            else:
                continue
        if number == total:
            print(number, "Is A Perfect Number.")
        else:
            print(number, "Is Not A Perfect Number.")
