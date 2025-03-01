from datetime import date

bugun = date.today()
print(bugun)
print(type(bugun)) # <class 'datetime.date'> 
print(bugun.day)
print(bugun.month)
print(bugun.year)
print(bugun.weekday()) # 0: Pazartesi, 6: Pazar
print(bugun.isoweekday()) # 1: Pazartesi, 7: Pazar 

gecmis_tarih = date(2005, 7, 15)
print(gecmis_tarih)
print(gecmis_tarih.weekday())

gecen_zaman = bugun - gecmis_tarih
print(gecen_zaman)
print(type(gecen_zaman)) # <class 'datetime.timedelta'>

#--------------------------------------------

from datetime import datetime

suan = datetime.now()
print(suan)
print(type(suan)) # <class 'datetime.datetime'>
print(suan.day)
print(suan.month)
print(suan.year)
print(suan.hour)
print(suan.minute)
print(suan.second)
print(suan.microsecond) 

print(suan.ctime())
print(suan.date())
print(suan.time())
print(suan.date().month)

print(suan.strftime('%d/%m/%Y %H:%M:%S'))


gecmis_an = datetime(2005, 7, 15, 5, 21, 45)
print(gecmis_an)

print(suan - gecmis_an)
print(type(suan - gecmis_an)) # <class 'datetime.timedelta'>

#--------------------------------------------

from datetime import datetime, timedelta

suan2 = datetime.now()
tdelta = timedelta(days=7, hours=12, minutes=30)
print(suan2)
print(suan2 + tdelta)
print(suan2 - tdelta)

#--------------------------------------------

# Project Euler Sorusu
# 20. Yüzyılda yani 1 OCAK 1901 ile 31 ARALIK 2000 arasında kaç defa bir ayın ilk günü Pazar gününe denk gelmiştir?

from datetime import date
ilk_tarih = date(1901, 1, 1)
son_tarih = date(2000, 12, 31)

pazar_gunu_sayisi = 0

for yil in range(ilk_tarih.year, son_tarih.year+1):
    for ay in range(1, 13):
        if date(yil, ay, 1).isoweekday() == 7:
            pazar_gunu_sayisi += 1
print(pazar_gunu_sayisi)

