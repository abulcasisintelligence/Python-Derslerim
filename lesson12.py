# Random Modülü Kullanımı

import random

# Her bir random fonksiyonu için ayrı listeler oluşturun
liste_random = []
liste_uniform = []
liste_randint = []
liste_randrange = []


# 10 kez döngü çalıştırın ve her bir random fonksiyonunun ürettiği değeri ilgili listeye ekleyin
for i in range(10):
    liste_random.append(random.random()) # 0.0 ile 1.0 arasında rastgele sayılar üretir.
    liste_uniform.append(random.uniform(10, 200)) # Belirlediğimiz aralıkta rastgele sayılar üretir.
    liste_randint.append(random.randint(10, 200)) # Belirlediğimiz aralıkta rastgele tam sayılar üretir. Her iki sınır da dahil.
    liste_randrange.append(random.randrange(10, 200, 2)) # Belirlediğimiz aralıkta rastgele sayılar üretir. Üçüncü parametre artış miktarını belirler.

# Listeleri ekrana yazdırın
print("liste_random:", liste_random)
print("liste_uniform:", liste_uniform)
print("liste_randint:", liste_randint)
print("liste_randrange:", liste_randrange)

#------------------------------------------------------------

liste_renkler = ["kırmızı", "mavi", "yeşil", "sarı", "mor", "turuncu", "siyah", "beyaz", "gri", "kahverengi"]

print(random.choice(liste_renkler)) # Liste içerisinden rastgele bir eleman seçer.
print(random.sample(liste_renkler, 3)) # Liste içerisinden belirtilen sayıda eleman seçer.
random.shuffle(liste_renkler) # Liste içerisindeki elemanları karıştırır.
print(liste_renkler)

#------------------------------------------------------------

# Zar atma simülasyonu

zarlar = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(1000):
    zar = random.randint(1, 6)
    zarlar[zar] += 1

for zar in zarlar:
    print(f"{zar} gelme olasılığı : %{zarlar[zar] / 100}")


#------------------------------------------------------------


# 10 defa 6-6 gelene kadar kaç deneme yapıldığını bulunuz.

alti_alti = 0
deneme_sayisi = 0

while True:
    deneme_sayisi += 1
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)
    if zar1 == 6 and zar2 == 6:
        alti_alti += 1
    if alti_alti == 10:
        print(f"10 defa 6-6 gelene kadar {deneme_sayisi} deneme yapıldı.")
        break