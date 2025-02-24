#integer, float ve type 

sayi1 = 5
sayi2 = 3.8
sayi3= 22/7

#python da float ve int'ın sayı sınırı yok
print(sayi3)
print(sayi3*sayi2)

#değişkenin tipini öğrenmek için type(sayi1) şeklinde öğrenebiliriz.

print(type(sayi2))  

#-------------------------------------------------------------------

# Matematiksel İşlemler
# "//" tam sayı bölmesi yapar ondalık kısmı atar.
# "** " kuvvetini alır.
# "abs" mutlak değer alır. 
# "round" yuvarlar.

print(51/4)
print(51//4)
print(5**3)
print(abs(-6))
sayi = 22/7
print(sayi)
print(round(sayi))

# Yuvarlarken virgülden sonraki bir basamaktan sonrasını yuvarlamak için print(round(sayi,n)) ile yapılır 'n' bir doğal sayı.

print(round(sayi,3))

# Python işlem önceliğine dikkat eder.

#-------------------------------------------------------------------

# Karşılaştırma Operatörleri 
# Eşit Eşittir "=="
# Küçük Eşittir "<="
# Büyük Eşittir ">="
# Eşit Değildir "!=" 
 
a=5
b=1

print(a == b)
print(a <= b)
print(a >= b)
print(a != b)

# İlk bir değişkeni tanımlayıp, farklı bir değişkeni ona eşitledikten sonra ilk değişkeni değiştirsen bile diğeri aynı kalır. Bellekte ilk olanı tutar. 
c=1
d=c
c=5
print("c:", c)
print("d:", d)

#-------------------------------------------------------------------


# String'i integer'a çevirmek için int fonksiyonu kullanılır ama string'in çevirilebilecek bir sayı olması gerekir.
# Ancak e eğer int olamayacak bir metin olsaydı çalışmazdı. örn: e = "100asd"

e = "100"
e2 = 100
e3 = int(e)
print(type(e))
print(type(e3))
print(e2 == e)
print(e2 == e3)

# int fonksiyonu içine ondalık sayı yazılabilir ama int ondalık kısmı atar. Yuvarlamaz.

e4 = int(7.8)
print(e4)

# integer'ı String'e çevirmek için str fonksiyonu kullanılır.

e5 = 123
e6 = str(e5)
print(type(e6))

#-------------------------------------------------------------------

# Bir değişkene bir sayı ile işlem yaptırıp yeniden tanımlamak istersek işlemin yanına = koyarak tekrar tanımlarız.

i = 5
i += 9
i2 = 3
i2 *= 4
i3 = 50
i3 //= 7
i4 = 2 
i4 **= 3
print(i)
print(i2)
print(i3)
print(i4)