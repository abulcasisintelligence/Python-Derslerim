import os

def file_class():
    folder = input("Klasörün yolunu giriniz: ").strip()  # Klasör yolunu alır ve boşlukları temizler
   
    # Klasör yolunun geçerli olup olmadığını kontrol et
    if not os.path.isdir(folder):
        print("Hata: Geçersiz klasör yolu!")
        return  # Programı durdur

    files = []  # Dosyaları tutacak liste
    extensions = []  # Dosya uzantılarını tutacak liste

    def list_dir():
        for file in os.listdir(folder):  # Belirtilen dizindeki dosyaları listeler ve bunlar içinde döner
            if os.path.isdir(os.path.join(folder, file)):  # Eğer bir klasörse
                continue
            else:  # Eğer bir dosya ise
                files.append(file)  # Dosyaları listeye ekler

    list_dir()  # Fonksiyonu çağırır

    # Dosya uzantılarını alma
    for file in files:  # Dosyalar içinde döner
        extension = file.split(".")[-1]  # Dosya adını ve uzantısını ayırır
        if extension in extensions:  # Eğer uzantılar listesinde varsa
            continue
        else:
            extensions.append(extension)

    # Uzantılara göre klasörler oluşturma
    for extension in extensions:
        if os.path.isdir(os.path.join(folder, extension)):
            continue
        else:
            os.mkdir(os.path.join(folder, extension))

    # Dosyaları klasörlere taşıma
    for file in files:
        extension = file.split(".")[-1]
        os.rename(os.path.join(folder, file), os.path.join(folder, extension, file))

if __name__ == "__main__":
    file_class()  # Fonksiyonu çağırır

