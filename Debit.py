print("""
******************************
Atm Makinesine Hosgeldiniz...

Islemler:

1. Bakiye Sorgulama

2. Para Yatirma

3. Para Cekme

Programdan Cıkmak Icin 'quit' yazın.
******************************

""")

bakiye = 10000

while True:
    islem = input("Islem Giriniz:")
    if islem == "1":
        print("Bakiyeniz:", bakiye, "TL")
    elif islem == "2":
        miktar = int(input("Yatirmak Istediginiz Miktari Giriniz:"))
        bakiye += miktar
        print("Bakiyenize", miktar, "TL Eklenmistir.")
    elif islem == "3":
        miktar = int(input("Cekmek Istediginiz Miktari Giriniz:"))
        bakiye -= miktar
        print("Bakiyenizden", miktar, "TL Cekilmistir.")
    elif islem == 'quit':
        print("Iyi Gunler Dileriz.")
        break
    else:
        print("Gecersiz Islem!")
