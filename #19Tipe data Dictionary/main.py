#Dictionary
member1 = {"ID":101,
           "Nama":"Muhammad Dhafin Rizqullah",
           "Pekerjaan":"Programmer",
           "Status Member":"Gold"}
member2 = {"ID":102,
           "Nama":"Dadang Konelo",
           "Pekerjaan":"Designer",
           "Status Member":"Platinum"}

#Cara membuat member list
memberList = {101:member1, 102:member2}

print(memberList[101])

#Cara mengakses nilai melalui key
print(member1["Nama"])
#melihat hanya key nya saja
print(member1.keys())
#melihat value nya saja
print(member1.values())
#melihat keys dan values
print(member1.items())