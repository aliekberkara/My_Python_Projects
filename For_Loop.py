sayilar = [1, 3, 5, 7, 9, 12, 19, 21] 

#Soru-1
# a) Sayılar Listesindeki Hangi Sayılar 3'ün Katıdır?

for kat in sayilar:
    if kat % 3 == 0:
        print(kat)

# b) Sayılar Listesindeki Sayıların Toplamı Nedir?

toplam = 0
for sayi in sayilar:
    toplam += sayi
print("Sayilarin Toplami:", toplam)

# c) Sayılar Listesindeki Tek Sayıların Karesini Alınız.

for sayi in sayilar:
    if sayi % 2 == 1:
        print(f"{sayi} Sayisinin Karesi: {sayi**2}")


sehirler = ['kocaeli', 'ankara', 'istanbul', 'izmir', 'rize']

# Soru-2 Şehirlerden Hangileri En Fazla 5 Karakterlidir?

for sehir in sehirler:
    if len(sehir) <= 5:
        print(sehir)

urunler = [
    {'name' : 'samsung S6', 'price' : '3000'},
    {'name' : 'samsung S7', 'price' : '4000'},
    {'name' : 'samsung S8', 'price' : '5000'},
    {'name' : 'samsung S9', 'price' : '6000'},
    {'name' : 'samsung S10', 'price' : '7000'}
]

# Soru-3
# a) Ürünlerin Fiyatları Toplamı Nedir?

fiyat = 0
for urun in urunler:
    fiyat += int(urun['price'])
print("Toplam Fiyatiniz:", fiyat)

# b) Ürünlerden Fiyatı En Fazla 5000 Olan Ürünleri Gösteriniz.

for urun in urunler:
    if int(urun['price']) <= 5000:
        print(urun['name'])
