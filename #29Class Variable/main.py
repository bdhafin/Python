class Mahasiswa():
    
    # jurusan = 'ekonomi'
    jumlahMahasiswa = 0

    def __init__(self, nama, nim):
        self.nama = nama #public variable
        self.nim = nim
        #cara mengakses class variable di dalam method
        Mahasiswa.jumlahMahasiswa += 1
    

dhafin = Mahasiswa('dhafin rizqullah', 10012443)
dhafin2 = Mahasiswa('dhafin rizqullah2', 10022443)
print(Mahasiswa.jumlahMahasiswa)






# #set class variable 
# Mahasiswa.jurusan = 'Internet'

# #ini sama dengan membuat variable instances (menimpa class variable)
# dhafin.jurusan = 'Hidup'

# #ini juga bisa digunakan untuk membuat variable instances
# dhafin.hobi = 'ngoding'

# #jika class variable maka bisa di akses seperti ini
# print(Mahasiswa.jurusan)

# print(dhafin.jurusan)

##Cara mengambil apa saja yang bisa di lakukan oleh sebuah variable
# print(Mahasiswa.__dict__)
# print(dhafin.__dict__)
