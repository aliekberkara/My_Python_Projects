'''
1-100 Arasında Rastgele Üretilecek Bir Sayıyı Aşağı Yukarı İfadeleri İle Bulmaya Çalışın.(Hak = 5)
** 'random modülü' İçin 'python random' Şeklinde Arama Yapın.
** 100 Üzerinden Puanlama Yapın. Her Soru 20 Puan.
** Hak Bilgisini Kullanıcıdan Alınız Ve Her Soru Belirtilen Can Sayısı Üzerinden Hesaplansın.
'''

import random

sayi = random.randint(1, 100)
hak = int(input("Can Sayisini Giriniz:"))
puan = 100
can = hak
while can > 0:
    print(f"**********************\nCan: {can}\n**********************")
    tahmin = int(input("Bir Sayi Tahmin Ediniz: "))
    
    if tahmin == sayi:
        print(f"**********************\nTebrikler, Sayiyi Bildiniz.\nPuaniniz: {puan}")
        break
    elif tahmin > sayi:
        print("**********************\nYanlis Tahmin.\nAsagi")
        can -= 1
        puan -= (100 / hak)
    else:
        print("**********************\nYanlis Tahmin.\nYukari")
        can -= 1
        puan -= (100 / hak)

if can == 0:
    print("Caniniz Bitti. Sayi:", sayi)