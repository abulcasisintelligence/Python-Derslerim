"""
# Dosya işlemleri
open()      # Dosya açmak için kullanılır. Dosya yoksa oluşturur.
read()      # Dosyanın içeriğini okumak için kullanılır.
write()     # Dosyaya veri yazmak için kullanılır.
close()     # Açık olan dosyayı kapatmak için kullanılır.
seek()      # Dosya içindeki imleci belirtilen konuma taşır.
tell()      # Dosya içindeki imlecin mevcut konumunu döner.
readline()  # Dosyadan bir satır okur.
readlines() # Dosyadan tüm satırları okuyup bir liste olarak döner.
writelines()# Bir liste içindeki verileri dosyaya yazar.

'r': Sadece okuma. Dosya yoksa hata verir.
'w': Sadece yazma. Dosya varsa içeriği siler, yoksa yeni dosya oluşturur.
'a': Sadece ekleme. Dosya varsa sonuna ekler, yoksa yeni dosya oluşturur.
'r+': Hem okuma hem yazma. Dosya yoksa hata verir.
'w+': Hem yazma hem okuma. Dosya varsa içeriği siler, yoksa yeni dosya oluşturur.
'a+': Hem ekleme hem okuma. Dosya varsa sonuna ekler, yoksa yeni dosya oluşturur.

"""

# f = open("example.txt", "r") # Dosyayı okuma modunda açar.
# content = f.read() # Dosyayı okur.
# print(content)
# f.close() # Dosyayı kapatır.
# Bu şekilde de kullanılabilir ama pratikte aç kapat yapmak yerine with kullanılır.

# with open("example.txt", "r", encoding="utf-8") as f: # Dosyayı açar. Bu blok içinde işlem yapılabilir dosyayı kapatmak gerekmez.
    # content = f.read()
    # print(content)
    # content2 = f.readlines()
    # print(content2)
    # for line in content2:
    #     print(line, end="") # end="" ile satır sonundaki boşlukları temizler.
    #     # print(line.strip()) # strip() metodu ile satır sonundaki boşlukları temizler.
    # for line in f: # Dosyayı satır satır okur.
    #     print(line.strip())
     
    # line= f.readline() # Dosyadan bir satır okur.
    # print(line, end="")
    # line= f.readline() # Dosyadan bir satır daha okur.
    # print(line, end="")
    # line= f.readline() # Dosyadan bir satır daha okur.
    # print(line, end="")
    # pozition = f.tell() # Dosya içindeki imlecin mevcut konumunu döner.
    # print(pozition)
    # f.seek(0) # Dosya içindeki imleci belirtilen konuma taşır.
    # line= f.readline() # Dosyadan bir satır okur.
    # print(line, end="")

    # content3 = f.read(10) # Dosyadan 10 karakter okur.
    # print(content3)
    # content4 = f.read(100) # Dosyadan 10 karakter daha okur.
    # print(content4)
    
    # read_amount = 10  # Okunacak karakter sayısı
    # content5 = f.read(read_amount) 
    # while len(content5) > 0:
    #     print(content5, end="")
    #     content5 = f.read(read_amount)

# Bu şekilde dosya tamamen baştan oluşturur yani içerik gider yeni yazdırdıklarınızı ekler.
# with open("example2.txt", "w", encoding="utf-8") as f2: 
#     f2.write("Merhaba Dünya\n")
#     f2.write("Python Programlama Dili\n")
#     f2.write("Öğreniyorum\n")

# # Bu şekilde dosyanın sonuna ekleme yapar.
# with open("example2.txt","a", encoding="utf-8") as f3:
#     f3.write("Yeni Satır Ekle\n")
#     f3.write("Yeni 2. Satır Ekle")

# with open("example2.txt", encoding="utf-8") as reading_file:
#     with open("example3.txt", "w", encoding="utf-8") as writing_file:
#         content6 = reading_file.readlines()
#         for line in content6:
#             writing_file.write(line) 
    
# with open("C:/Users/Hp/Desktop/MY WORKS/Deneme Klasörü/deneme2/teymen.png", "rb") as reading_photo:
#     with open("C:/Users/Hp/Desktop/MY WORKS/Deneme Klasörü/deneme2/teymen2.png", "wb") as writing_photo:
#         reading_amount = 1024
#         content7 = reading_photo.read(reading_amount)
#         while len(content7) > 0:
#             writing_photo.write(content7)
#             content7 = reading_photo.read(reading_amount)
# print("Dosya Kopyalandı")

with open("C:/Users/Hp/Desktop/MY WORKS/Deneme Klasörü/deneme2/teymen.png", "rb") as reading_photo:
    with open("C:/Users/Hp/Desktop/MY WORKS/Deneme Klasörü/deneme2/teymen3.png", "wb") as writing_photo:
      for line in reading_photo:
          writing_photo.write(line)    



    



