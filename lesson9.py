#  İlk 10.000 asal sayıynın kaç tanesi 3 ile başlar 7 ile biter.

from traceback import print_exc


prime_list = list()

prime_list.append(2) 

sayi = 3

while True:
    prime = True
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            prime = False
            break
    if prime:
        prime_list.append(sayi)
        if len(prime_list) == 10000:
            break
    sayi += 1

list2 = list()

for prime in prime_list:
    str_prime = str(prime)
    # if str_prime[0] == '3' and str_prime[-1] == '7': bu şekilde de olabilirdi.
    if str_prime.startswith('3') and str_prime.endswith('7'):
        list2.append(prime)

print(list2)
print(len(list2))
       
#------------------------------------------------------------

#  3 basamaklı sayıların kaç tanesi rakamlarının küpleri toplamına eşittir.

liste = list()
for sayi in range(100, 1000):
    toplam = 0
    gecici_sayi = sayi
    while gecici_sayi != 0:
        basamak = gecici_sayi % 10
        toplam += basamak ** 3
        gecici_sayi //= 10
    if toplam == sayi:
        liste.append(sayi)
print(liste)

#------------------------------------------------------------


#  Fibonacci dizisi ilk iki terimi 1 olan ve sonraki terimi önceki iki terimin toplamı olan bir dizidir.
#  İlk 100 fibonacci sayısını ekrana yazdır.

fibonacci_list= [1, 1]

# index = 2
# while True:
#     fibonacci_list.append(fibonacci_list[index - 1] + fibonacci_list[index - 2])
#     index += 1
#     if index == 100:
#         break
# print(fibonacci_list)

for i in range(2,100):
    fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])

print(fibonacci_list)

#------------------------------------------------------------

# 100 basamaklı ilk fibonacci sayısını bulunuz.

fibonacci_list = [1, 1]
index = 2
while True:
    fibonacci_list.append(fibonacci_list[index-1] + fibonacci_list[index-2])
    sayi = fibonacci_list[-1]
    if len(str(sayi)) == 100:
        break
    index += 1
print(sayi)
print(index)
