"""
Find if a given number is prime or not.
** Prime Numbers Are Numbers That Have No Exact Divisors Except 1 And Itself.
"""

number = int(input("Enter A Number: "))
prime = 0
if number == 0 or number == 1:
    print(f"{number} Is Not A Prime Number.")

elif number == 2:
    print(f"{number} Is A Prime Number.")

elif number > 2 and number % 2 == 1:
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            prime += 1
    if prime == 0:
        print(f"{number} Is A Prime Number.")
    else:
        print(f"{number} Is Not A Prime Number.")