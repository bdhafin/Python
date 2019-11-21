#bentuk dasar while
# while expression:
#     pass

angka = 0

while angka < 5:
    print("nilai angka adalah", angka)
    angka += 1

print('di luar while')

#while dengan argument boolean
start = True
angka = 0

while start:
    print('di dalam while')
    if angka is 100:
        start = False
        print('angka 100 ditemukan')
    angka += 1