import os
import datetime

def file_class():
    folder = input("Klasörün yolunu giriniz: ").strip()  # Klasör yolunu alır ve boşlukları temizler
   
    # Klasör yolunun geçerli olup olmadığını kontrol et
    if not os.path.isdir(folder):
        print("Hata: Geçersiz klasör yolu!")
        return  # Programı durdur

    files = []  # Dosyaları tutacak liste
    file_creation_dates = []  # Dosya oluşturulma tarihlerini tutacak liste

    def list_dir():
        for file in os.listdir(folder):  # Belirtilen dizindeki dosyaları listeler ve bunlar içinde döner
            if os.path.isdir(os.path.join(folder, file)):  # Eğer bir klasörse
                continue
            else:  # Eğer bir dosya ise
                files.append(file)  # Dosyaları listeye ekler

    list_dir()  # Fonksiyonu çağırır

    # Dosya oluşturulma tarihini alma
    for file in files:  # Dosyalar içinde döner
        timestamp = os.path.getctime(os.path.join(folder, file)) # Dosyanın oluşturulma tarihini alır
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y-%H-%M') # Tarihi okunabilir bir formata çevirir
        if date not in file_creation_dates:
            file_creation_dates.append(date)
    
    # Oluşturulma tarihlerine göre klasörler oluşturma
    for date in file_creation_dates:
        date_folder = os.path.join(folder, date)
        if not os.path.isdir(date_folder):
            os.mkdir(date_folder)
    
    # Dosyaları klasörlere taşıma
    for file in files:
        timestamp = os.path.getctime(os.path.join(folder, file))
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y-%H-%M')
        os.rename(os.path.join(folder, file), os.path.join(folder, date, file))

if __name__ == "__main__":
    file_class()  # Fonksiyonu çağırır