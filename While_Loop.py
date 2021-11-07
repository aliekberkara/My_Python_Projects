sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# Soru-1 Listesini While İle Ekrana Yazdırınız.

n = 0
while n < len(sayilar):
    print(sayilar[n])
    n += 1

# Soru-2 Başlangıç Ve Bitiş Değerlerini Kullanıcıdan Alıp Aradaki Tüm Tek Sayıları Ekrana Yazdırınız.

ilk = int(input("Baslangic Degerini Giriniz:"))
son = int(input("Bitis Degerini Giriniz:"))

while ilk <= son:
    if ilk % 2 == 1:
        print(ilk)
    ilk += 1
print("Bitti.")

# Soru-3 1-100 Arasındaki Sayıları Azalan Şekilde Yazdırınız.

sayi = 100
while sayi > 0:
    print(sayi)
    sayi -= 1

# Soru-4 Kullanıcıdan Alacağınız 5 Sayıyı Ekranda Sıralı Bir Şekilde Yazdırınız.

liste = []
i = 0
while i < 5:
    liste.append(int(input("Bir Sayi Giriniz:")))
    i += 1
print(*sorted(liste))


# Soru-5 Kullanıcıdan Alacağınız Ürün Bilgilerini Ürünler Listesi İçerisinde Saklayınız.
# **Ürün Sayısını Kullanıcıya Sorun.
# **Dictionary Listesi (name, price) Şeklinde Olsun.
# **Ürün Ekleme İşlemi Bittiğinde Ürünleri Ekranda While İle Listeleyiniz.

urunler = []

adet = int(input("Urun Sayisini Giriniz:"))

while adet > 0:
    name = input("Urun Adini Giriniz:")
    price = input("Urunun Fiyatini Giriniz:")
    urunler.append({'name' : name, 'price' : price})
    adet -= 1

for urun in urunler:
    print(urun)