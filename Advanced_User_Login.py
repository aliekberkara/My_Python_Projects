print("------------ Kullanici Girisi ------------")

kullanici = 'michael65'
parola = '3773146ali'
giris = 3

while True:
    ad = input("Kullanici Adinizi Giriniz:")
    sifre = input("Parolanizi Giriniz:")
    if kullanici != ad and parola == sifre:
        print("Hatali Giris!!!\nKullanici Adi Hatali!!!")
        giris -= 1
    elif kullanici == ad and parola != sifre:
        print("Hatali Giris!!!\nParola Hatali!!!")
        giris -= 1
    elif kullanici != ad and parola != sifre:
        print("Hatali Giris!!!\nKullanici Adi ve Parola Hatali!!!")
        giris -= 1
    else:
        print("Basarili Giris!!!\nSisteme Giris Yapildi!!!")
        break
    if giris == 0:
        print("Fazla Sayida Deneme Yapildi!!!")
        break
