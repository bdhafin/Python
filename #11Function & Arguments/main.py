#Fungsi dengan menggunakan argument sederhana
def siswa(nama):
    print('siswa ini bernama:', nama)

siswa('mario')

#fungsi dengan menggunakan keywords arguments
print('*'*50)
def guru(nama, pelajaran):
    print('guru ini bernama:', nama)
    print('mengajar:', pelajaran)

guru(nama='popong', pelajaran='seni rupa')
guru(pelajaran='olahraga', nama='endang')

# fungsi dengan menggunakan default arguments
print('*'*50)
def penjaga_sekolah(nama, shift='siang', sifat='baik'):
    print('penjaga sekolah ini bernama:', nama)
    print('shift:', shift)
    print('sifat:', sifat)

penjaga_sekolah('Entis')
penjaga_sekolah('Roni', shift='malam')
penjaga_sekolah('Asep', sifat='galak sekali')

