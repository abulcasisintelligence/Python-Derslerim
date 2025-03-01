import os 

# mkdir, bir klasör oluşturur.
# makedirs, birden fazla iç içe klasör oluşturur.
# rmdir, bir klasörü siler.
# removedirs, birden fazla iç içe klasörü siler.
# remove, bir dosyayı siler.
# listdir, dosyaları listeler.
# getcwd, bulunduğunuz dizini gösterir.
# chdir, dizin değiştirir.
# open, dosya oluşturur.
# close, dosyayı kapatır.
# write, dosyaya yazı yazar.
# read, dosyayı okur.
# w, dosyayı yazma modunda açar.
# r, dosyayı okuma modunda açar.
# w+, dosyayı hem okuma hem yazma modunda açar.
# r+, dosyayı hem okuma hem yazma modunda açar.

print(os.getcwd())

# \ kullanırsanız hata alırsınız. / kullanmalısınız ya da \\ kullanmalısınız.
# os.chdir("C:\\Users\\Hp\\Desktop\\MY WORKS\\CAS\\ilkproje\\Downloads3DModels") # Doğru kullanım
# os.chdir("C:/Users/Hp/Desktop/MY WORKS/CAS/ilkproje/Downloads3DModels")  # Doğru kullanım
# os.chdir("C:\Users\Hp\Desktop\MY WORKS\CAS\ilkproje\Downloads3DModels")  # Yanlış kullanım

# Ya da bunlar yerine aşağıdaki gibi de kullanabilirsiniz.
os.chdir(r"C:\Users\Hp\Desktop\MY WORKS\CAS\python_deneme_klasor") # Doğru kullanım. r ile başlayan string ifadelerde \ işareti sorun oluşturmaz.
print(os.getcwd())

print(os.listdir()) # Dosyaları listeler.
print(os.listdir(r"C:\Users\Hp\Desktop\MY WORKS\CAS\python_deneme_klasor")) # Dosyaları listeler.

for dosya in os.listdir():
    print(dosya)

# os.mkdir("Deneme Klasörü") # Yeni bir klasör oluşturur.

""" for dosya in os.listdir():
    for i in range(1, 6):
        os.mkdir(f"Deneme Klasörü {i}") """

# os.makedirs("Deneme Klasörü 1/Alt Klasör 1/Alt Klasör 2") # Birden fazla alt alta klasör oluşturur.

# os.rmdir("Deneme Klasörü") # Klasörü siler.

# os.removedirs("Deneme Klasörü 1/Alt Klasör 1/Alt Klasör 2") # Birden fazla alt alta klasörü siler.
# yeni_dosya = open("yeni_dosya.txt", "w") # Dosya oluşturur. "w" dosyayı yazma modunda açar. "r" dosyayı okuma modunda açar.


# os.chdir(r"C:\Users\Hp\Desktop\MY WORKS\CAS\python_deneme_klasor\Deneme Klasörü 2")
# yeni_dosya = open("yeni_dosya.txt", "w+") # Dosya oluşturur. "w+" dosyayı hem okuma hem yazma modunda açar.
# yeni_dosya.write("Bu bir deneme dosyasıdır.") # Dosyaya yazı yazar.
# yeni_dosya.read() # Dosyayı okur. Sadece "w" modunda açılan dosyaları okuyamazsınız.
# yeni_dosya.close() # Dosyayı kapatır.
# print(os.listdir()) # Dosyaları listeler.

# # os.remove("yeni_dosya.txt") # Dosyayı siler.
# silinecek = os.listdir()[0]
# os.remove(silinecek) # Dosyayı siler.
# print(os.listdir()) # Dosyaları listeler.

# os.rmdir(r"C:\Users\Hp\Desktop\MY WORKS\CAS\python_deneme_klasor\Deneme Klasörü 2") # Klasörü siler.

# os.rename("yeni_dosya.txt", "yeni_dosya2.txt") # Dosyanın adını değiştirir.
print(os.listdir()) # Dosyaları listeler.

# os.mkdir("Deneme Klasörü 2") # Yeni bir klasör oluşturur.
os.chdir(r"C:\Users\Hp\Desktop\MY WORKS\CAS\python_deneme_klasor\Deneme Klasörü 2")
yeni_dosya = open("yeni_dosya.txt", "w+") # Dosya oluşturur. "w+" dosyayı hem okuma hem yazma modunda açar.
yeni_dosya.write("Bu bir deneme dosyasıdır.") # Dosyaya yazı yazar.
yeni_dosya.close() # Dosyayı kapatır.
print(os.listdir()) # Dosyaları listeler.

# os.rename("yeni_dosya.txt", "yeni_dosya2.txt") # Dosyanın adını değiştirir.
# print(os.listdir()) # Dosyaları listeler.

os.chdir(r"C:\Users\Hp\Desktop\MY WORKS\CAS\python_deneme_klasor")

# os.rename("yeni_dosya2.txt", "C:/Users/Hp/Desktop/MY WORKS/CAS/python_deneme_klasor/Deneme Klasörü 3/yeni_dosya2.txt") # Klasörün konumunu da bu şekilde değiştirebiliriz.
# print(os.listdir()) # Dosyaları listeler.

print(os.stat("Deneme Klasörü 3/yeni_dosya2.txt")) # Dosya hakkında bilgi verir.
print(os.stat("Deneme Klasörü 3/yeni_dosya2.txt").st_size) # Dosyanın boyutunu verir.
print(os.stat("Deneme Klasörü 3/yeni_dosya2.txt").st_mtime) # Dosyanın değiştirilme tarihini verir.

from datetime import datetime
print(datetime.fromtimestamp(os.stat("Deneme Klasörü 3/yeni_dosya2.txt").st_mtime)) # Dosyanın değiştirilme tarihini verir.


# os.walk, iç içe klasörleri ve dosyaları listeler.
for gecerli_klasor, alt_klasor, dosyalar in os.walk(r"C:\Users\Hp\Desktop\MY WORKS\CAS\python_deneme_klasor"):
    print(f"Şu anki klasör: {gecerli_klasor}")
    print(f"Alt klasörler: {alt_klasor}")
    print(f"Dosyalar: {dosyalar}")
    print("\n")

print(os.path.join("Deneme 1", "Deneme 2","Deneme 3")) # Dosya yolu oluşturur. Bu klasörlerden herhangi birinin başına / koyarsanız ondan öncekileri göstermez.
print(os.path.isfile("Deneme Klasörü 3/yeni_dosya2.txt")) # Dosya mı değil mi kontrol eder.
print(os.path.isdir("Deneme Klasörü 3")) # Klasör mü değil mi kontrol eder.

print(os.path.splitext("Deneme Klasörü 3/yeni_dosya2.txt")) # Dosyanın adını ve uzantısını ayırır.

