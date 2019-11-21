###Cara pertama
# import matematika

# matematika.tambah(3, 4)

####Cara kedua (memakai as)
# import matematika as math

# math.tambah(3, 4)
# math.kurang(8, 4)

###Cara ketiga (spesifik fungsi)
#from matematika import * -> Cara ambil semua fungsi
# from matematika import tambah, kurang

# tambah(3, 4)
# kurang(8, 4)

###Cara keempat (spesifik fungsi dengan as)
from matematika import tambah as t
 
t(3, 4)