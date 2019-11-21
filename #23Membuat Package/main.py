###Cara import melalui package
# from sains import fisika, matematika

# fisika.kecepatan(3, 4)
# matematika.tambah(3, 4)

### import dengan __init__
# import sains

# sains.tambah(3, 4)

### Cara lain import dengan __init__
from sains import tambah, kecepatan

tambah(3, 4)
kecepatan(6, 5)

#import package dari luar
import math

print(math.cos(3.14))