# For range
# for i in range(0,40):
#     print(i)


#For range dengan increment
# for i in range(10,40,5):
#     print(i)

number = 25
#For range dengan if
for i in range(0, 40):
    print(i)
    if i is number:
        print("angka ditemukan", i)
        #cara keluar dari for ketika kondisi tertentu
        break
#Mengecek looping sampai akhir atau tidak (jika looping selesai maka ini akan di eksekusi)
else:
    print('angka tidak di temukan')