# 1,1,2,3,5,8,13,21,34.............

while True:
    print("----------- Fibonacci Program -----------\nType 'quit' to exit.")
    number = input("Enter A Number: ")
    a = 1
    b = 1

    fibonacci = [a, b]
    if number == 'quit':
        print("We Hope You Come Again...")
        break
    else:
        number = int(number)
        for i in range(number - 2):
            a, b = b, a + b
            fibonacci.append(b)
        print(*fibonacci)
