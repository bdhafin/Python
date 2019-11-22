print("ini adalah program pembagian")

while True:
    #contoh try except biasa
    try:
        penyebut = int(input("masukan angka penyebut: "))
        pembilang = int(input("masukan angka pembilang: "))
        hasil = penyebut / pembilang
        break
    ##mengambil exception menjadi error
    # except Exception as err:
    #     print(err) 
    #menangkap error tertentu
    except ValueError:
        print("Yang anda masukan bukan angka")
    except ZeroDivisionError:
        print("angka pembilang yang anda masukan adalah nol")
    #bentuk dasar
    except:
        print("Error")

print("berhasil, hasil pembagian adalah", hasil)