import math

sonuç = math.sqrt(16)
print(sonuç)

#  from math import sqrt şeklinde de kullanılabilir.
#  Bu durumda math.sqrt(16) yerine sadece sqrt(16) şeklinde kullanılabilir. 

from math import sqrt
sonuç2 = sqrt(25)
print(sonuç2) 

#------------------------------------------------------------


# import my_module
import my_module as mdl # my_module.py dosyasını mdl olarak kısa isim vererek import ettik.
sonuç3 = mdl.cember_cevre(4)
print(sonuç3)
sonuç4 = mdl.cember_alan(4)
print(sonuç4)