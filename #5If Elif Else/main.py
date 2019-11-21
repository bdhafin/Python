nilai = 75
# nilai2 = 80

#Contoh nesting if
# if nilai1 == 75:
#    print("nilai anda : ", nilai1)
#    print("Step 1")
#    if nilai2 == 80:
#        print("nilai anda : ", nilai2)
#        print("Step 2")

# is sama kaya ==
if nilai is 75:
   print("nilai anda : ", nilai)

# is not sama kaya !=
if nilai is not 60:
     print("nilai anda : ", nilai)

print("==" * 50)
#Contoh penerapan if dan elif

nilaiUjian = 70

if 80 <= nilaiUjian <= 100:
    print("nilai anda adalah A")
elif 70 <= nilaiUjian < 80:
    print("Nilai anda adalah B")
elif 60 <= nilaiUjian < 70:
    print("Nilai anda adalah C")
elif 50 <= nilaiUjian < 60:
    print("Nilai anda adalah D, lalukan perbaikan")
else:
    print("maaf anda tidak lulus mata kuliah ini")

print("*" * 100)
print("Operator logika untuk list dan string\n")

gorengan = ['bakwan', 'cireng', 'bala-bala', 'gehu', 'combro', 'pisang goreng', 'pukis', 'risoles']
beli =  'cireng'

#Cara mencari sebuah elemen dari list dengan if
if beli in gorengan:
    print("Ya saya ada jual", beli)

#Cara lain untuk else
if not beli in gorengan:
    print("Gaada saya jual", beli)

#Cara mencari sebuah karakter di sebuah string
karakter = 'z'
if karakter in beli:
    print("ada ", karakter, " di ", beli)
else:
    print("tidak ada", karakter, "di", beli)