# Sözlükler 
# küme parantezi içinde yazılır. İlk anahtar sözcük yani key yazılır. Sonra ":" ile değer yani value yazılır.
# key string yapısında olmak zorundadır ama value herhangi bir yapıda olabilir.

kisi ={"isim" : "Ali", "yas" : 20, "cinsiyet" : "m", "hobiler"  : ["Sinema", "Konser", "Yazılım"]}

print(kisi)
print(kisi["cinsiyet"])
print(kisi["hobiler"])

# print(kisi["key"]) dict in içine keyleri yazarak istediğimiz değeri görebiliriz.

kisi["isim"] = "Ahmet" #Bu şekilde istediğimiz key'in değerini değiştirebiliriz.
print(kisi)

# Aynı anda birden fazla değeri değiştirmek için .update yapsıı kullanılır.

kisi.update({"isim" : "Ayşe", "yas" : 25, "cinsiyet" : "w"})
print(kisi)

kisi["id"] = 12345 #Herhangi olmayan bir key ile değeri eklemek için bu şekilde kisi["key"] = value ile ekleyebiliriz.
print(kisi)

del kisi["id"] # istediğimiz herhangi bir alanı silmek için de del fonksiyonu kullanırız.
print(kisi)

for i in kisi: # Bu şekilde tanımlarsak bize alt alta key'leri yazdırır.
    print(i)
for x in kisi: # Bu şekilde tanımlarsak alt alta value'leri yazdırır.
    print(kisi[x])

print(kisi.values()) # Sadece value'lerden oluşan bir dict verir.
print(kisi.keys()) # Sadece key'lerden oluşan bir dict verir.
print(kisi.items()) # key ve value'leri ikili şekilde verir.

for k in kisi.items():
    print(k)

for k,v in kisi.items():
    print(k,":",v)

# print(kisi["id"]) şeklinde tanımlı olmayan bir keyi bu şekilde sorgularsak kod hata verir.
# Bunun için .get() fonksiyonu kullanılır. kisi.get("key","mesaj") bu şekilde key yerine aramak istediğimiz keyi yazıp, mesaj yerine de eğer yoksa yazmasını istediğimiz bir metni koyabiliriz. Koymazsak da none verir hat vermez. 

print(kisi.get("isim"))
print(kisi.get("yas","bulunamadı"))
print(kisi.get("id"))
print(kisi.get("id","bulunamadı"))
