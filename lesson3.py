# Listeler

import enum


renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil", "Kırmızı"]
sayilar =[1, 2, 3, 8, 75, 45]

print(len(renkler))
print(renkler[3])
print(renkler[2:])
print(renkler[1:4])
print(renkler[:3])

# print(renkler[_:_:_]) birinci aralık başlangıç, ikinci aralık bitiş, üçüncü aralıkta kaçar kaçar olamsını istediğimiz kıdımdır.

print(renkler[::2])
print(renkler[1::2])
print(renkler[1:4:2]) 

#---------------------------------------------------------

# .append metodu listenin sonuna eleman eklemek için kullanılır.
# .insert metodu araya istediğimiz yere eleman eklemek için kullanılır. renkler.insert(n,"Gri") n hangi indekse istersek o sayı.
# .remove ile istediğimiz elemanı sileriz.
print(renkler)
renkler.append("Gri")
print(renkler)
renkler.insert(2,"Ela")
print(renkler)
renkler.remove("Ela")
print(renkler)
renkler.remove(renkler[6])
print(renkler)

#---------------------------------------------------------

ekrenkler = ["Turuncu", "Lacivert", "Mor"]

# .extend bir listeye liste şeklinde eleman eklerken kullanılır. renkler.extend(renkler2) şeklinde.
# .extend yerine .append de kullanılabilir ama append listenin içine bir elemanı liste olarak ekler.

renkler.extend(ekrenkler)
print(renkler)
del renkler[6:9] #Birden fazla eleman silmek için del operatörü kullanılır. 
renkler.append(ekrenkler) # type: ignore
print(renkler)

#---------------------------------------------------------

# .pop(i) Belirtilen i index'indeki elemanı kaldırır ve döndürür. .pop() şeklinde bırakılırsa sonraki elemanı siler.

silinen = renkler.pop()
print(renkler)
print(silinen)
silinen2 = renkler.pop(2)
print(renkler)
print(silinen2)

renkler.insert(2, silinen2)

#---------------------------------------------------------

# .reverse Listenin elemanlarını tersine çevirir. Orijinal listeyi değiştirir! Geri dönüş değeri None dır.

renkler.reverse()
print(renkler)

renkler.reverse()

#---------------------------------------------------------

# .sort() Listenin sırasını kalıcı olarak değiştirir. Varsayılan olarak alfabetik veya küçükten büyüğe sıralama yapar. reverse=True parametresi ile büyükten küçüğe sıralama yapılabilir
# .sort(reverse = True) ile listeyi varsayılanın tam tersi reverse=True parametresi ile büyükten küçüğe sıralama yapılabilir
# .sort() listeyi kalıcı olarak değiştirir reverse gibi. Eğer kalıcıolarak değiştirmek istemezsek sorted() kullanmalıyız.

renkler3 = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil", "Kırmızı"]
renkler3.sort()
print(renkler3)
renkler3.sort(reverse = True)
print(renkler3)

renkler4 = sorted(renkler)
print(renkler)
print(renkler4)


#---------------------------------------------------------

# min() max() fonksiyonları lsite içindeki alfabetik en baştaki sondaki ya da sayılarda en büyük en küçük olanları döndürür.

print(min(renkler))
print(max(renkler))
print(min(sayilar))
print(max(sayilar))

# sum() toplam donksiyonudur. Eğer stringler den oluşan listeyse hata alırız.

print(sum(sayilar))

for i in renkler:
    print(i)

print(list(enumerate(renkler)))               # Numaralandırma fonksiyoudur.
print(list(enumerate(renkler, start=3)))      # Başlangıç sayısını start ile belirleyebiliriz.

print("Siyah" in renkler) # in ile list içinde elemanın olup olamdığını sorgulayabiliriz.
print("Gri" in renkler)

#---------------------------------------------------------

# Listeyi string'e çevirmek için join metodu kullanılır. stringrenkler = "_".join(renkler) dediğimizde list'i stringe çevirir. Aralarına da _ yerine ne koyarsak onu koyar

stringrenkler = "".join(renkler)
print(stringrenkler) 
stringrenkler = " ".join(renkler)
print(stringrenkler) 
stringrenkler = "_".join(renkler) 
print(stringrenkler) 
stringrenkler = ",".join(renkler)
print(stringrenkler)  
stringrenkler = " - ".join(renkler)
print(stringrenkler)  

# Bir string halindeki listeyi de list e çevirmek için split kullanılır.
# yenidenrenkler = stringrenkler.split(" - ") şeklinde liste oluşturabiliriz. split in içine nereden bölmek istiyorsak oradaki işaretleri yazmalıyız.
# Örneğin stringrenkler = ",".join(renkler) ise Siyah,Beyaz,Sarı,Mavi,Yeşil,Kırmızı böyle olur bunu bölmek için yenidenrenkler = stringrenkler.split(",") şeklinde yapmalıyız.

yenidenrenkler = stringrenkler.split(" - ")
print(yenidenrenkler)