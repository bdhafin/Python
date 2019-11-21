# #List sebagai iterable
# gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']

# #Bentuk dasar for loop
# for g in gorengan:
#     print(g)
#     print(len(g))

# #string sebagai iterable
# bakwan = 'bakwan'

# for i in bakwan:
#     print(i)

#For di dalam for
gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']
buah = ['semangka', 'jeruk', 'apel', 'anggur']
sayur = ['kangkung', 'wortel', 'tomat', 'kentang']

daftar_belanja = [gorengan,buah,sayur]

for subDaftarBelanja in daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)

