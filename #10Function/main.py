# #Bentuk dasar fungsi
# def fungsi():
#     pas

#Cara mendefinisikan fungsi
def fungsi():
    print('ini adalah fungsi')

#Cara memanggil fungsi
fungsi()

#Membuat fungsi sederhana
def suara_ayam():
    print('kukuruyuk!!!!')

def harga_ayam():
    #memanggil fungsi di dalam fungsi
    suara_ayam()
    print('harga ayam per 1 kg adalah Rp. 20.000')

#Membuat fungsi dengan input argument
def harga_total_ayam(kg):
    suara_ayam()
    harga = 20000
    hargaTotal = kg * harga
    print('Harga', kg, 'kg ayam adalah',hargaTotal)

harga_ayam()
#memanggil fungsi dengan argument
harga_total_ayam(4)