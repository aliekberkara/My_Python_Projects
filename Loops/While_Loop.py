numbers = [1, 3, 5, 7, 9, 12, 19, 21]

# Problem 1
# Print the "numbers" List with "While".

n = 0
while n < len(numbers):
    print(numbers[n])
    n += 1
print("------------------------------")

# Problem 2
# Get the start and end values from the user and print all the odd numbers on the screen.

first = int(input("Enter the Initial Value: "))
end = int(input("Enter the End Value: "))

while first <= end:
    if first % 2 == 1:
        print(first)
    first += 1
print("Finished.")
print("------------------------------")

# Problem 3
# Print the numbers 1-100 in descending order.

number = 100
while number > 0:
    print(number)
    number -= 1
print("------------------------------")

# Problem 4
# Print the 5 numbers you will receive from the user on the screen in a sequential manner.

sequence = []
i = 0
while i < 5:
    sequence.append(int(input("Enter A Number: ")))
    i += 1
print(*sorted(sequence))
print("------------------------------")


# Problem 5
# Keep the Product Information You Will Get from the User in the Products List.
# **Ask User for Product Number.
# **As Dictionary List (name, price).
# **When Adding a Product is Finished, List the Products with "While" on the Screen.

products = []

amount = int(input("Enter Number of Products:"))

while amount > 0:
    name = input("Enter the Product Name:")
    price = input("Enter the Price of the Product:")
    products.append({'name' : name, 'price' : price})
    amount -= 1

for product in products:
    print(product)