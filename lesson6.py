# Koşullu Durumlar (if, elif, else)
# "if" belirli bir koşul sağlanıyorsa çalışır.
# "elif" (else if) üstteki "if" koşulu sağlanmadığında yeni bir koşul kontrol eder.
# "else" hiçbir koşul sağlanmazsa çalışır.

x = 10

y = 20

if x > y:
    print("x, y'den büyüktür.")
elif x == y:
    print("x ve y eşittir.")
else:
    print("x, y'den küçüktür.")

#-------------------------------------------------------------------

# Mantıksal Operatörler (and, or, not)
# "and" iki koşulun da doğru olması gerekir.
# "or" herhangi bir koşulun doğru olması yeterlidir.
# "not" koşulun tersini alır.

a = 5
b = 10
c = 15

if a < b and b < c:
    print("Hem a, b'den küçük hem de b, c'den küçük.")

if a > b or b < c:
    print("a, b'den büyük ya da b, c'den küçük.")

if not (a > b):
    print("a, b'den büyük değildir.")

#-------------------------------------------------------------------

# "in" Anahtar Kelimesi Kullanımı
# "in" belirli bir öğenin listede, tuple'da veya string içinde olup olmadığını kontrol eder.

meyveler = ["elma", "armut", "muz"]

if "elma" in meyveler:
    print("Elma listede var.")

isim = "Furkan"

harf1 = "f"
harf2 = "F"

# Büyük küçük  harf duyarlılığı vardır.

if harf1 in isim:
    print("'f' isimde geçiyor.")
else:
    print("'f' isimde geçmiyor.")

if harf2 in isim:
    print("'F' isimde geçiyor.") 
else:
    print("'F' isimde geçmiyor.")

#-------------------------------------------------------------------

# "is" Anahtar Kelimesi Kullanımı
# "is" iki değişkenin aynı nesneyi bellekte tutup tutmadığını kontrol eder.
# Yani iki ifadenin eşit değil özdeş olması gerekiyor bellekte birbirlerine eşitlenmiş olmalıdır.
# id lerinin aynı olup olmadığını kontrol eder.

a = [1, 2, 3]
b = a

print(a is b)  # True (Aynı nesneye referans verirler.)

c = [1, 2, 3]
print(a is c)  # False (İçerikler aynı olsa da farklı nesneler.)

name1 = "furkan"
name2 = "furk"

name2 += "an"

print("name1 id: ", id(name1))
print("name2 id: ", id(name2))

if name1 == name2:
    print("'==' ile kontrol : name1 ile name2 aynıdır.")
else:
    print("'==' ile kontrol : name1 ile name2 farklıdır.")

if name1 is name2:
    print("'is' ile kontrol : name1 ile name2 aynıdır.")
else:
    print("'is' ile kontrol : name1 ile name2 farklıdır.")


#-------------------------------------------------------------------

# Örnek Uygulama
# Kullanıcının girdiği sayının pozitif, negatif veya sıfır olup olmadığını kontrol eden kod

sayi = int(input("Bir sayı giriniz: "))

if sayi > 0:
    print("Pozitif bir sayı girdiniz.")
elif sayi < 0:
    print("Negatif bir sayı girdiniz.")
else:
    print("Girdiğiniz sayı sıfırdır.")
