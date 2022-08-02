import numbers


def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Number must be integer...")
    
    if not number >= 0:
        raise ValueError("Number must be zero or positive...")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number-1)
    return inner_factorial(number)
try:
    print(factorial(int(input("Number: "))))
except Exception as ex:
    print(ex)