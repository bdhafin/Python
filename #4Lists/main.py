#Bentuk dasar list
Data = [1, 4, 9, 16, 25, 36, 49, 64]

#Mengakses Nilai pada list
SubData = Data[0]

#Mengakses Nilai pada list(dari belakang)
SubData2 = Data[-3]

#Mengakses dengan panjang tertentu
SubData3 = Data[0:4]

#Mengakses dari element ke - n sampai akhir
SubData4 = Data[2:]
# SubData4 = Data[-2:]
# SubData4 = Data[:2]

Data2 = [100, 200, 300, 400, 500, 600, 700, 800]

#Menambah lists
Data3 = Data + Data2

#Merubah content dari list
Data[4] = 90

#Cara memindahkan data pada lists
a = Data[:]
#Cara lain
# a = Data.copy()
a[7] = 87

#Merubah content lists dengan menggunakan metode slicing
Data[3:5] = [11,12]

#List dalam list
x = [Data, Data2]

#Mengakses list dalam multidimensional list
y = x[0][3]

####### Method untuk list #######
#Menambahkan data di belakang
Data.append(30)

###### Function untuk list ######
#mengukur panjang list
panjang_list = len(Data)

print(panjang_list)
