class Mahasiswa():
    nama = 'nama'

    #Membuat method
    def belajar(self, kondisi):
        #akses self nama
        print(self.nama, 'sedang belajar', kondisi)
    
    def tidur(self):
        print(self.nama, 'sedang tidur di kelas')

dhafin = Mahasiswa()

#set attribute
dhafin.nama = 'dhafin'
print(dhafin.nama)

#Memanggil method
dhafin.belajar('dengan giat')
dhafin.tidur()