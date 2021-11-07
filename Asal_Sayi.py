"""
Girilen Bir Sayının Asal Olup Olmadığını Bulun.
** Asal Sayı 1 Ve Kendisi Hariç Tam Böleni Olmayan Sayılara Denir.
"""

sayi = int(input("Bir Sayi Giriniz:"))
asal = 0
if sayi == 0 or sayi == 1:
    print(f"{sayi} Asal Sayi Degildir.")

elif sayi == 2:
    print(f"{sayi} Asal Sayidir.")

elif sayi > 2 and sayi % 2 == 1:
    for i in range(2, (sayi // 2) + 1):
        if sayi % i == 0:
            asal += 1
    if asal == 0:
        print(f"{sayi} Asal Sayidir.")
    else:
        print(f"{sayi} Asal Sayi Degildir.")