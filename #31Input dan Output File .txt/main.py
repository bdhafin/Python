# Input dan output file


#membuat file text

"""
    w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan di buat file baru
    r = read mode only / hanya bisa baca
    a = apppending mode / menambahkan data di akhir baris
    r+ = write and read mode
"""
#open file
file = open("data.txt", "w")

#menulis ke file
file.write("Ini adalah data text yang di buat dengan menggunakan python")
file.write("\nini baris kedua")
file.write("\nini baris ketiga")
file.write("\nini baris keempat")

#menutup file
file.close()

# membaca file text

file2 = open('data.txt', 'r')

# print(file2.read()) -> read biasa
# print(file2.read(10)) -> hanya 10 karakter
print(file2.readline()) #membaca baris

file2.close()

# appending mode

file3 = open('data.txt', 'a')

file3.write("\nbaris ini di buat dengan menggunakan mode append")

file.close()