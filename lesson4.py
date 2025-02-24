# Tuple (demet) oluştururken list lerden farklı olarak [] yerine () kullanılır.
# List ten en büyük farkı kalıcı olarak oluşturulmasıdır değiştirilemezler. insert, remove vs. gibi fonksiyonlar kullanılamaz.
demet = ("Sarı", "Mavi", "Kırmızı", "Siyah", "Yeşil")
print(len(demet))
print(list(demet))
print(type(demet))

#------------------------------------------------------------------

# Kümelerde sıra yoktur tuple ve listler den farkı odur. Örneğin for döngüsünü art arda çalıştırırsak her biri farklı sırada olur.

kume = {"Sarı", "Mavi", "Kırmızı", "Siyah", "Yeşil"}

for i in kume:
    print(i)

kume.add("Mor") # Kümeye yeni eleman ekler.
print(kume)
kume.remove("Sarı") # Kümeden eleman silmek için kullanılabilir.
print(kume)
#.discard da eleman silmek için kullanılır. .remove dan farkı örneğin buradaki gibi kümede olamyan elemanı silmeye çalıştığımızda discard hata vermez remove hata verir.
kume.discard("Mor")
print(kume)
kume.discard("Gri") 

#------------------------------------------------------------------

# .intersection kumelerin kesişimini verir.
# .union kumelerin birleşimini verir.
# .differance kümelerin farkını verir. 
kume1= {"Sarı", "Mavi", "Kırmızı", "Siyah", "Yeşil", "Turuncu"}
kume2= {"Sarı", "Mavi", "Kırmızı", "Gri", "Lacivert", "Mor"}

print(kume1.intersection(kume2))
print(kume1.union(kume2))
print(kume1.difference(kume2))
print(kume2.difference(kume1))

print("Siyah" in kume2)
print("Beyaz" in kume2.union(kume1))
print("Kırmızı" in kume1.intersection(kume2))

# List ve Tuple iki farklı şekilde oluşturulabilir ancak Küme tek farklı şekilde oluşturulabilir.
bosliste1 = list()
bosliste2 = []

bostuple1 = tuple()
bostuple2 = ()

boskume1 = set() # Boş bir küme oluşturur.
boskume2 = {} # Bir Dictionary Sözlük oluşturur.

print(type(bosliste1)) # <class 'list'>
print(type(bosliste2)) # <class 'list'>
print(type(bostuple1)) #<class 'tuple'>
print(type(bostuple2)) #<class 'tuple'>
print(type(boskume1)) #<class 'set'>
print(type(boskume2)) #<class 'dict'>

# set()fonksiyonu içine list, tuple, string de versek onları parçalayıp küme haline getirir.

python = set("Python")
print(python)

python2 = set(demet)
print(python2) 

python3 = set([1, 2, 3, 25, 865])
print(python3)