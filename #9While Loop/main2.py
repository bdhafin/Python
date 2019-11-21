#else, break, continue dan pass
angka = 0

while angka < 10:
    if angka is 5:
        # break

        # angka += 1 -> jika tidak di beri ini maka continue di while akan infinite loop
        # continue

        pass

    print("nilai angka adalah", angka)
    angka += 1
else:
    print('nilai angka di akhir while adalah', angka)

print('==== di luar while ====')