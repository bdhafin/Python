# set = himpunan 
# #Cara 1 membuat set
# superHero = {'wiro sableng',
#              'si buta dari gua hantu', 
#              'saras 008', 'gundala', 
#              'gatot kaca'}

# superHero.add('mak lampir')
# #tidak akan di anggap karena sudah ada
# superHero.add('gundala')

superHero = set()

superHero.add('wiro sableng')
superHero.add('gundala')
superHero.add('saras 008')
#bisa di campur
superHero.add(18)

print(superHero)

#Cara sort himpunan / set
# print(sorted(superHero))

ganjil = {1, 3, 5, 7, 9}
genap = {2, 4, 6, 8, 10}
prima = {2, 3, 5, 7}

#menggabung 2 set
print(ganjil.union(genap))
#Mencari irisan dari 2 set
print(ganjil.intersection(prima))