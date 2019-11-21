#fungsi dengan return value
def kuadrat(argument):
    total = argument ** 2
    print('nilai kuadrat dari', argument, 'adalah', total)
    return total #ini adalah contoh return

a = kuadrat(3)
print(a)

#Cara lain
# print(kuadrat(4))

print('=' * 50)

#fungsi dengan return value dan multiple argument
def tambah(argument1, argument2):
    total = argument1 + argument2
    print(argument1, '+', argument2, '=', total)
    return total

def kali(argument1, argument2):
    total = argument1 * argument2
    print(argument1, 'x', argument2, '=', total)
    return total

b = kali(3, tambah(3, 4))