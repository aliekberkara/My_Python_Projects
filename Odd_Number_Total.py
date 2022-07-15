# Write a program that returns the sum of odd numbers up to a number received from the user.
total = 0
def sum(number):
    global total
    if number % 2 == 0:
        return sum(number - 1)
    if (number < 1):
        return total
    total += number
    return sum(number - 2)
    

number = int(input('Enter a number: '))
print(f'Sum: {sum(number)}')