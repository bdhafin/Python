import sys

data_list = [1,2,3,4,5,6,7,8,9,10,"pisang goreng", "dhafin", "rizqullah", False, 3.14]
data_tuple = (1,2,3,4,5,6,7,8,9,10,"pisang goreng", "dhafin", "rizqullah", False, 3.14)

#mengambil besarnya data dari sebuah data
besar_data_list = sys.getsizeof(data_list)
besar_data_tuple = sys.getsizeof(data_tuple)

print("besar dari list:", besar_data_list)
print("besar dari tuple:", besar_data_tuple)