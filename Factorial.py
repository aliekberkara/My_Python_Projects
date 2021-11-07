print("""
*******************
Factorial Finder Program


Type 'quit' to quit...
*******************
""")

while True:
    number = input("Enter A Number: ")
    if number == 'quit':
        print("See You.")

    else:
        number = int(number)
        if number >= 0:
            factorial = 1
            for i in range(2, number + 1):
                factorial *= i
            print(f"{number}! = {factorial}")
            print("Number of Characters: ", len(str(factorial)))
        else:
            print("Please Enter A Positive Number!!!")
