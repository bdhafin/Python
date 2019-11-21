def tambah(a, b):
    print(a, ' +', b, '=', a + b)

def kurang(a, b):
    print(a, ' -', b, '=', a - b)

print(__name__) #hasil nya __main__

def main():
    print('ini adalah fungsi utama dari matematika')

#mengecek bahwa ini di jalankan di file utama dan bukan di file lain
if __name__ == '__main__':
    main()