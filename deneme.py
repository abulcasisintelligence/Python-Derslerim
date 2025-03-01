from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np

# Resim dosyasının yolunu belirtin
image_path = "C:/Users/Hp/Desktop/MY WORKS/Deneme Klasörü/deneme2/teymen.png"

# Resmi aç ve gri tonlamaya çevir
image = Image.open(image_path).convert("L")
image_array = np.array(image)

# SVD hesapla
U, S, Vt = np.linalg.svd(image_array, full_matrices=False)

# Kullanıcıdan kaç singular value kullanmak istediğini sor
num_singular_values = int(input("Kaç singular value kullanmak istiyorsunuz? (1-{}): ".format(len(S))))

# Seçilen singular value'lar ile yeni bir resim oluştur
S_new = np.zeros_like(S)
S_new[:num_singular_values] = S[:num_singular_values]
new_image_array = U @ np.diag(S_new) @ Vt
new_image = Image.fromarray(new_image_array.astype(np.uint8))

# Yeni resmi kaydet
new_image_path = "C:/Users/Hp/Desktop/MY WORKS/Deneme Klasörü/deneme2/teymen_svd.png"
new_image.save(new_image_path)

# Matplotlib ile göster
plt.imshow(new_image, cmap="gray")
plt.axis("off")
plt.show()
