numbers = [1, 3, 5, 7, 9, 12, 19, 21] 

#Problem 1
# a) Which Numbers in the "numbers" List are Multiples of 3?

for multiple in numbers:
    if multiple % 3 == 0:
        print(multiple)
print("------------------------")

# b) What is the Sum of Numbers in the "numbers" List?

total = 0
for number in numbers:
    total += number
print("Sum Of Numbers: ", total)
print("------------------------")

# c) Square the Odd Numbers in the "numbers" List

for number in numbers:
    if number % 2 == 1:
        print(f"Square Of The Number {number} :  {number**2}")
print("------------------------")


cities = ['kocaeli', 'ankara', 'istanbul', 'izmir', 'rize']

# Problem 3
# Which Cities Have Maximum 5 Characters?

for city in cities:
    if len(city) <= 5:
        print(city)
print("------------------------")

products = [
    {'name' : 'samsung S6', 'price' : '3000'},
    {'name' : 'samsung S7', 'price' : '4000'},
    {'name' : 'samsung S8', 'price' : '5000'},
    {'name' : 'samsung S9', 'price' : '6000'},
    {'name' : 'samsung S10', 'price' : '7000'}
]

# Soru-3
# a) What is the sum of the prices of the products?

price = 0
for product in products:
    price += int(product['price'])
print("Your Total Price: ", price)
print("------------------------")

# b) Show the products with a maximum price of 5000 TL from the products.

for product in products:
    if int(product['price']) <= 5000:
        print(product['name'])
