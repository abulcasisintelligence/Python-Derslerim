# Fonksyonlar
# Fonksyonlar, belirli bir işi yapmak için kullanılan kod bloklarıdır.
# def anahtar_kelime ile tanımlanırlar. def fonksiyon_adi(): şeklinde tanımlanırlar.

def bilgi_ver():
    print("Bu bir bilgi mesajıdır.")

bilgi_ver()

# Fonksyonlar parametre alabilir. Parametreler fonksiyonun parantezleri içine yazılır.
alinan_isim = input("İsminizi giriniz: ")

def buyuk_harf_yap(alinan_isim):
    return alinan_isim.capitalize() # return anahtar kelimesi ile fonksiyonun sonucu değiştirilir.
isim = buyuk_harf_yap(alinan_isim)

def selamla(isim):
    print(f"Merhaba {isim}")
selamla(isim)

girdi = input(f"{isim}, lütfen arasında boşluk bırakarak iki sayı gir: ")

# Girdiyi boşluk karakterine göre ayırın
x_str, y_str = girdi.split()

# Ayırdığınız değerleri x ve y olarak atayın
x = int(x_str)
y = int(y_str)

def toplam(x, y):
    print(f"Bu iki sayının toplamı = {x + y}")

toplam(x, y)

alinan_sayilar = input(f"{isim}, ortalamsını almak istediğiniz sayıları arasında boşluk bırakarak giriniz: ")

# Girdiyi boşluk karakterine göre ayırın
sayilar = alinan_sayilar.split()
liste = list()
for sayi in sayilar:
    liste.append(int(sayi))

def ortalama_hesapla(liste):
    toplam =sum(liste)
    adet = len(liste)
    ortalama = toplam / adet
    print(f"Bu sayıların ortalaması = {ortalama}")

ortalama_hesapla(liste)