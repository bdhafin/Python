class Mahasiswa():
    
    jurusan = 'tata boga'
    __nilai = 0 #private variable

    def __init__(self, nama, nim):
        self.nama = nama #public variable
        self.nim = nim

    def uts(self, inputNilai):
        self.__nilai += inputNilai
    
    def uas(self, inputNilai):
        self.__nilai += inputNilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama, "Tidak Lulus")
        else:
            print(self.nama, "Lulus")

dhafin = Mahasiswa('dhafin rizqullah', 10012443)

dhafin.uts(30)
dhafin.uas(50)

dhafin.check_status()