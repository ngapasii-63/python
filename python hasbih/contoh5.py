y = 12
x = 10
print('x berisi angka',x, 'desimal atau', bin(x), 'biner')
print('y berisi angka', y, 'desimal atau', bin(y), 'biner')
print('\n')
print('x & y', x & y)
print('x | y', x | y)
print('x^y :',x^y)
print('~x :',~x)
print('x << 1:',x << 1)
print('x >> 1 :',x >> 1)

print('Hasil dari True and True :', True and True)
print('Hasil dari True and False:', True and False)
print('Hasil dari False and True :', False and True)
print('Hasil dari False and False:', False and False)
print('\n')

print('Hasil dari True or True :', True or True)
print('Hasil dari True or False', True or False)
print('Hasil dari False or True :', False or True)
print('Hasil dari False or False:', False or False)

print('\n')
print('Hasil dari not True :', not True)
print('Hasil dari not False', not False)

 #Contoh Operasi
hasil = (5 > 6) and (10 <= 8)
print (hasil)
hasil = ('budiluhur' == 'budiluhur') or (10 <= 8)
print (hasil)
hasil = not (10 < 10)
print (hasil)
hasil = ('budiluhur' == 'budiluhur') and (10 <= 8) or (1!= 1)
print (hasil)