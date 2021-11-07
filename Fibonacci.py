# 1,1,2,3,5,8,13,21,34.............

while True:
    print("----------- Fibonacci Programi -----------\n Cikis Yapmak Icin 'quit' Yaziniz.")
    sayi = input("Bir Sayi Giriniz:")
    a = 1
    b = 1

    fibonacci = [a, b]
    if sayi == 'quit':
        print("Tekrar bekleriz...")
        break
    else:
        sayi = int(sayi)
        for i in range(sayi - 2):
            a, b = b, a + b
            print("a:", a, "b:", b)
            fibonacci.append(b)
        print(*fibonacci)
