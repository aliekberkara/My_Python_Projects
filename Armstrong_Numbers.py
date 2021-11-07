"""
Problem 2

Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı
( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

while True:
    sayi = int(input("Bir Sayi Giriniz:"))
    b_sayisi = len(str(sayi))
    b_sayi = sayi
    toplam = 0

    while b_sayi > 0:
        basamak = b_sayi % 10
        b_sayi = (b_sayi - basamak) / 10
        toplam += basamak ** b_sayisi

    if toplam == sayi:
        print(f"{sayi} Sayisi Armstrong Sayisidir...")
        break
    else:
        print(f"{sayi} Sayisi Armstrong Sayisi Degildir...")
        break
