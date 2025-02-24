# Listeler ve For Döngüsü
# "for" döngüsü bir liste, tuple, string veya herhangi bir iterable üzerinde döner.

takimlar = ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor"]

for takim in takimlar:
    print(takim)

#-------------------------------------------------------------------

# Range Fonksiyonu ve For Döngüsü
# "range" belirli bir aralıkta sayı üretmek için kullanılır.
# range(start, stop, step) şeklinde kullanılır. İlk sınır dahil son sınır dahil değildir.

for i in range(5):  # 0'dan 4'e kadar olan sayıları yazdırır.
    print(i)

for i in range(2, 10, 2):  # 2'den 10'a kadar 2'şer artarak gider. 2 den başlar ikişer ikişer 10 a gelirse durur. 10 u yazdırmaz.
    print(i)

rakam = 1

for i in range(0,10):
    rakam *= 2 # 2 ile 0 dan 9 a kar
    # print("i: ", i)

print(rakam)
#-------------------------------------------------------------------

# İç İçe For Döngüleri
# Bir döngü içerisinde başka bir döngü kullanabiliriz.

for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

#-------------------------------------------------------------------

# Break ve Continue Anahtar Kelimeleri
# "break" döngüyü tamamen sonlandırır.
# "continue" döngünün o anki iterasyonunu atlar ve bir sonraki iterasyona geçer.

for i in range(10):
    if i == 5:
        break  # 5'e geldiğinde döngü sonlanır.
    print(i)

for i in range(10):
    if i % 2 == 0: # % n kullanılırken solundaki sayının n ile bölümünden kalanı bulur. Burada 2 ile bölümünden kalanın 2 olup olmadığını sorguluyor.
        continue  # Çift sayıları atlar, sadece tek sayıları yazdırır.
    print(i)

liste = [1,2,3,4,5,6,7,8,9]
print("Liste:")
for k in liste:
    if k == 5:
        continue
    print(k)
#-------------------------------------------------------------------

# While Döngüsü
# "while" döngüsü belirli bir koşul sağlandığı sürece çalışır.

x = 0
while x < 5:
    print("x: ", x)
    x += 1  # Sonsuz döngüye girmemesi için x'in değerini arttırıyoruz.
#-------------------------------------------------------------------

# Sonsuz Döngü ve Dikkat Edilmesi Gerekenler
# Sonsuz döngüye girmemek için while döngüsünde koşulun bir noktada False olacağından emin olun.

# while True:
#     print("Bu bir sonsuz döngüdür.")  # Sonsuz döngüye dikkat edin.

#-------------------------------------------------------------------

a1 = 1
while True:
    if a1 == 500:
        break
    if a1 % 2 != 0:
        a1 += 1
        continue
    print(a1)
    a1 += 1
    