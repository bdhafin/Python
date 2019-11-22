class Mahasiswa():
    nama = 'nama'
    
    #membuat __init__
    def __init__(self, nama, nim):
        #memasukan variable dari init ke self variable
        self.nama = nama
        self.nim = nim

    def belajar(self, kondisi):
        print(self.nama, 'sedang belajar', kondisi)
    
    def tidur(self):
        print(self.nama, 'sedang tidur di kelas')

dhafin = Mahasiswa('dhafin rizqullah', 10012443)
print('nama :', dhafin.nama)
print('nim :', dhafin.nim)

dhafin.belajar('dengan malas')
# dhafin.nama = 'dhafin'