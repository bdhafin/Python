class Ojek():
    
    def __init__(self, nama, tipeMotor, daerah):
        self.nama = nama
        self.tipeMotor = tipeMotor
        self.daerah = daerah

    def cek_id_supir(self):
        print('nama :', self.nama, '\nmotor :', self.tipeMotor, '\ndaerah :', self.daerah)
        print("=" * 50)

#ini adalah inherintace
class Gojek(Ojek):
    
    #override method
    def cek_id_supir(self):
        print("cek aplikasi gojek")
    
ojek1 = Ojek('mario', 'kopling', 'bandung')
ojek2 = Gojek('jackson', 'matic', 'cimahi')

ojek1.cek_id_supir()
ojek2.cek_id_supir()