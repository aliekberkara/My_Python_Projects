"""
Problem 4 Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir
değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
"""

toplam = 0
while True:
    sayi = input("Bir Sayi Giriniz:")
    if sayi == 'q':
        print(f"Toplam:{toplam}")
        break
    else:
        sayi = int(sayi)
        toplam += sayi
