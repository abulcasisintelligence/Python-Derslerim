print("something") 
print('something')
# "" ve ya '' kullanmak da sorun yok ama ' işaretini içinde kullanmak zorunda kalırsan olmaz.
# print('Ali'nin evi') olmaz eğer yine de böyle kullanmak istiyorsan
print('Ali\'nin evi') 
# şeklinde kullanmak gerekir \ kendinden sonraki sembolün bir anlamı olmadığını belirtir.

print("""Merhaba
Dünya""")
print("Merhaba\nDünya")
# Alt satıra geçerek yazmak için """ veya \n ile geçilebilir.

print("Merhaba\tDünya")
# \t ise bir tab boşluk bırakır.

x = "Furkan Star"
y = "Naber"

print(x + " " + y)

print(x[1])
print(x[1:4])
print(x[::3])
print(x[::-1])
# x değişkeninin n'inci karakterini dödürmek için [n] kullanılır. -n tersten n'inci karakteri yazdırır.
# x değişkeninin m ile n'inci karakter arasını dödürmek için [m:n] kullanılır. m dahil n değil.
# [::n] x değişkeninin 0. terimden başlayarak n'in katları olan karakterlerini yazdırır.
# [::-1] x'i tersten yazdırır.

print(x.upper()) # x.upper() x'i büyük harflerle yazma metodu
print(x.lower()) # x.lower() x'i küçük harflerle yazma metodu
print(x.capitalize()) # x.capitalize() x'in baş harfini büyük harfle yazma metodu

print(x.startswith("ab.."))
print(x.endswith("ab.."))
# x'in herhangi bir kelime/katrakter ile başlayıp başlamadığını kontrol etme metodu
# örn: print(x.startswith("Fur")) True  print(x.startswith("fur")) False

print(len(x)) # x'in kaç karakter olduğunu görme

print(x * 3) # print(x * n ) x'i art arda n kere yazdırır. (n sayı)

print("{} {} nasılsın".format(x,y))
print(f"{x} {y} nasılsın")
# Bu iki şekilde de kümelerin yerlerine istediğin değişkeni yazdırabiliriz. 