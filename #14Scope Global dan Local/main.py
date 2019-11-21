# scope variable 

namaKucing = 'pretty'
makananKucing = 'royal canin'

def rubah_nama_kucing(namaBaru):
    # ini variable local
    namaKucing = namaBaru
    print('Saya rubah nama kucing menjadi', namaKucing)

def kasih_makan_kucing(makanan, nama):
    #mengakses variable global (scope global)
    global namaKucing,makananKucing
    namaKucing = nama
    makananKucing = makanan

rubah_nama_kucing('mimi')
kasih_makan_kucing('universal', 'Jimmy')
print('Nama kucing saya menjadi', namaKucing,'dan makan', makananKucing)