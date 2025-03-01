# Time Modülü Kullanımı

import time
""" 
zaman = time.time() # 1 Ocak 1970 tarihinden bu yana geçen saniye cinsinden zamanı verir.
print(zaman)

#------------------------------------------------------------
# Bir kodun başındn ve sonundaki zaman farkını hesaplayarak kodun çalışma süresini ölçebiliriz.
# Bu sayede kodun ne kadar sürede çalıştığını ölçebiliriz ve kodun performansını test edebiliriz.

baslangıc = time.time()
liste = []

for i in range(100000):
    liste.append(i)

bitis = time.time()
print("Geçen süre:", bitis - baslangıc)

#------------------------------------------------------------

simdiki_zaman = time.ctime() # Şu anki zamanı verir.
print(simdiki_zaman)

zaman_farki = time.ctime(10000) # 1 Ocak 1970 tarihinden parantez içindeki sayı kadar (10000 saniye) sonrasını verir.
print(zaman_farki)

#------------------------------------------------------------

local_time = time.localtime() # Yerel saat bilgisini verir.
print(local_time)
print(local_time.tm_year) # Yıl bilgisini verir.
print(local_time.tm_mon) # Ay bilgisini verir.
print(local_time.tm_mday) # Gün bilgisini verir.
print(local_time.tm_hour) # Saat bilgisini verir.
print(local_time.tm_min) # Dakika bilgisini verir.
print(local_time.tm_sec) # Saniye bilgisini verir.

print(time.asctime(local_time)) # Yerel saat bilgisini okunabilir bir şekilde verir.

#------------------------------------------------------------

"""
# time.strftime() fonksiyonu ile iSTEDİĞİMİZ bir formatta zamanı alabiliriz.
# time.strftime(format, t) şeklinde kullanılır. format parametresi zorunludur. t parametresi ise opsiyoneldir.
# format parametresi ile belirtilen formatta zamanı verir. t parametresi ise zamanı verir. Eğer t parametresi verilmezse şu anki zamanı verir.

zaman2 = time.strftime("%d.%m.%Y %H:%M:%S") # Belirtilen formatta zamanı verir.
print(zaman2)

print("Program başladı.")
time.sleep(5) # Belirtilen saniye kadar programı duraklatır.
print("Program bitti.")
