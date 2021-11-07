"""
Problem 1

Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""
while True:
    toplam = 0
    sayi = input("Bir Sayi Giriniz:(Cikis Yapmak Icin 'quit' Yaziniz.)")
    if sayi == 'quit':
        print("Tekrar Bekleriz...")
        break
    else:
        sayi = int(sayi)
        for i in range(1, (sayi // 2) + 1):
            if sayi % i == 0:
                toplam += i
            else:
                continue
        if sayi == toplam:
            print(sayi, "Mukemmel Sayidir...")
        else:
            print(sayi, "Mukemmel Sayi Degildir...")
