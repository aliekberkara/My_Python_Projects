print("""
*******************
Faktoriyel Bulma Programi


Cikmak Icin 'quit' yazın...
*******************
""")

while True:
    sayi = input("Bir sayi giriniz:")
    if sayi == 'quit':
        print("Gorusmek uzere")

    else:
        sayi = int(sayi)
        if sayi >= 0:
            faktoriyel = 1
            for i in range(2, sayi + 1):
                faktoriyel *= i
            print(f"{sayi}! = {faktoriyel}")
            print("Karakter Sayisi:", len(str(faktoriyel)))
        else:
            print("Lutfen Pozitif Bir Sayi Giriniz!!!")
