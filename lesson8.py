
"""
# Kullanıcıdan alınan input her zaman string olarak alınır.
# Kullanıcıdan alınan inputu integer'a çevirmek için int() fonksiyonu kullanılır.
# Kullanıcıdan alınan inputu float'a çevirmek için float() fonksiyonu kullanılır. 
sayi = int(input("Bir sayı giriniz: "))  # Kullanıcıdan bir sayı al

# Faktöriyel hesaplama

i = 1
faktoriyel = 1

while i <= sayi:
    faktoriyel *= i  # Faktöriyele çarp
    i += 1  # 'i'yi arttır ki döngü ilerlesin

print(f"{sayi}! = {faktoriyel}")  # Sonucu yazdır



for i in range(1, sayi + 1):
    faktoriyel *= i

print(f"{sayi}! = {faktoriyel}")

#-----------------------------------------------------


# Kullanıcıdan alınan sayının asal olup olmadığını bulma

sayi2 = int(input("Bir sayı giriniz: "))  
prime = True

for i in range(2, sayi2):
    if sayi2 % i == 0:
        prime = False
        break
if prime:
    print(f"{sayi2} asaldır.")
else:
    print(f"{sayi2} asal değildir.")

#-----------------------------------------------------

# Kullanıcıdan alınan sayının pozitif bölen sayısını bulma

sayi3 = int(input("Bir sayı giriniz: "))
bolen_sayisi = 0

for i in range(1, sayi3 + 1):
    if sayi3 % i == 0:
        bolen_sayisi += 1
print(f"{sayi3} sayısının pozitif bölen sayısı: {bolen_sayisi}")

#-----------------------------------------------------

# Kullanıcıdan alınan sayının rakamları toplamını bulma.

sayi4 = input("Bir sayı giriniz: ")
toplam = 0

for rakam in sayi4:
    toplam += int(rakam) # rakam değişkeni string olduğu için integer'a çeviriyoruz.
print(f"{sayi4} sayısının rakamları toplamı: {toplam}")

# yeni_sayi = int(sayi4)
# while yeni_sayi != 0:
#     rakam = yeni_sayi % 10
#     toplam += rakam
#     yeni_sayi //= 10
# print(f"{sayi4} sayısının rakamları toplamı: {toplam}")

#-----------------------------------------------------

# Kullanıcıdan 5 sayı alıp bu sayıları küçükten büyüğe sıralama.
liste = []

for sayi5 in range(5):
    get_sayi = int(input(f"{sayi5 + 1}. sayıyı giriniz: "))
    liste.append(get_sayi)

print("Listeniz: ", liste)  # Listeyi yazdır
print("En büyük sayı: ", max(liste))  # Listede en büyük sayıyı bul
print("En küçük sayı: ", min(liste))  # Listede en küçük sayıyı bul
liste.sort() # Listeyi küçükten büyüğe sırala
print("Sıralanmamış liste: ", liste)

#-----------------------------------------------------

# Kullanıcıdan alınan sayıyın bir sayının karesi olup olmadığını bul.
# Eğer bir sayıyın karesi ise karesi alınan sayıyı ve karekökünü yazdır.

sayi6 = int(input("Bir sayı giriniz: "))

# for i in range(1, sayi6):
#     if i * i == sayi6:
#         print(f"{sayi6} sayısı {i} sayısının karesidir.")
#         print(f"{i} sayısının karekökü: {i}")
#         break
# else:
#     print(f"{sayi6} sayısı bir sayının karesi değildir.")

karekok = sayi6 ** 0.5

if int(karekok) == karekok:
    print(f"{sayi6} sayısı {int(karekok)} sayısının karesidir.")
else:
    print(f"{sayi6} sayısı bir sayının karesi değildir.")

#-----------------------------------------------------

# Kullanıcıdan alınan metnin içinde hangi harfin kaç kere kullanıldığını bulma.

metin = input("Bir metin giriniz: ")
sozluk = dict()

# harf = input("Hangi harfin kaç kere kullanıldığını öğrenmek istiyorsunuz: ")
# for karakter in metin:
#     if karakter in sozluk:
#         sozluk[karakter] += 1
#     else:
#         sozluk[karakter] = 1

# if harf in sozluk:
#     print(f"{harf} harfi {sozluk[harf]} kere kullanılmıştır.")
# else:
#     print(f"{harf} harfi metinde bulunmamaktadır.")

for harf in metin:
    if harf in sozluk:
        sozluk[harf] += 1
    else:
        sozluk[harf] = 1
for karakter, adet in sozluk.items():
    if karakter.isalpha(): # isalpha() metodu karakterin harf olup olmadığını kontrol eder.
        print(f"{karakter} harfi {adet} kere kullanılmıştır.")
    elif karakter.isdigit(): # isdigit() metodu karakterin rakam olup olmadığını kontrol eder.
        print(f"{karakter} sayısı {adet} kere kullanılmıştır.")
    else:
        print(f"{karakter} işareti {adet} kere kullanılmıştır.")

#-----------------------------------------------------

# Kullanıcıdan alınan metindeki a harflerini büyük A yapma.

metin2 = input("Bir metin giriniz: ")

yeni_metin = ""

for harf in metin2:
    if harf == "a":
        yeni_metin += "A"
    else:
        yeni_metin += harf

print(yeni_metin)

#-----------------------------------------------------

"""

# Kullanıcıdan alınan metindeki kelimelerin ilk harflerini büyük yapma.

metin3 = input("Bir metin giriniz: ")

yeni_metin2 = ""

for kelime in metin3.split():
    yeni_metin2 += kelime.capitalize() + " "
print(yeni_metin2.strip())