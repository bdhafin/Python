#Teknik Looping

nama_orang = ['Dhafin', 
              'Rizqulah',
              'Didin Jamprut',
              'Agus Koli',
              'Asep Sugus']

kumpulan_sekolah = ['smkn 1 cimahi',
                    'sman 1 cimahi',
                    'smkn 2 cimahi',
                    'man 2 cimahi',
                    'sma terbuka 1']
#Cara menampilkan index dalam for
for i,nama in enumerate(nama_orang):
    print(i," ", nama)
print("="*50)

#Menggabungkan 2 data dalam 1 looping
for nama, sekolah in zip(nama_orang, kumpulan_sekolah):
    print(nama, "sekolah di", sekolah)
print("="*50)

nama_kota = {'cimahi', 'bandung', 'jakarta', 'purwakarta', 'karawang'}

#Cara looping set
# for kota in nama_kota:

#Cara looping dengan soted
for kota in sorted(nama_kota):
    print(kota)
print("="*50)
#dictionary

lokasi_sekolah = {'Cimahi': 'SMKN 1 Cimahi',
               'Bandung': 'SMKN 1 Bandung',
               'Jakarta': 'SMAN 1 Jakarta'}

#Hanya mengambil keys
# for i in lokasi_sekolah.keys():
#     print(i)

#Hanya mengambil values
# for i in lokasi_sekolah.values():
#     print(i)

#Mengambil items (keys dan values)
for i,v in lokasi_sekolah.items():
    print(i, " ", v)
print("="*50)

#For dengan di reverse
for i in reversed(range(1,10,1)):
    print(i)
