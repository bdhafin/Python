barang = ['kunci', 'ember', 'jaket', 'ban', 'mobil']
print(barang)

####beberapa method yang bisa digunakan untuk memanipulasi list
#menambah data list di belakang (append)
barang.append('sepeda')
print(barang)

#menambahkan data secara iterable string
barang.extend('dompet')
print(barang)

#menambahkan data dengan posisi tertentu
barang.insert(3, 'sepeda')
print(barang)

#Menghitung elemen tertentu di dalam list
jumlahSepeda = barang.count('sepeda')
print('jumlah sepeda adalah:', jumlahSepeda)

#menghapus data (hanya menghapus data yang di temukan pertama kali)
barang.remove('sepeda')
print(barang)

#membalikkan data pada list
barang.reverse()
print(barang)

#mengcopy data dari list ke list lain
print("*" * 50)
stuff = barang.copy()
stuff.append('gelas')
print(stuff)