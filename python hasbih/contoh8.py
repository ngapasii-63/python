tuple1 = ('Doni Kusuma', 'Anton Wijaya', 'Kimia', 1997, 2020)
tuple2 = (1, 2, 3, 4, 5)
tuple3 = ("a", "b", "c", "d", "e")
#mengakses isi Tuple
print ("Isi tuple[1]: ", tuple1)
print ("Isi tuple [1:3] : ", tuple2)
print ("Isi tuple [3:] : ", tuple3)

print("Program deret aritmatika")
print("======")
sukuAwal = input("Masukkan suku awal : ")
beda = input("Masukkan beda: ")
banyak = int(input("Masukkan banyak deret: "))
jumDeret = banyak + 1
suku = int(sukuAwal)
jum = 0
for i in range(1, jumDeret, 1) :
    print("Suku ke-", i, "=", suku)
    suku = suku + int(beda)
    jum = jum + 1
print("Jumlah deret = ", jum)

for i in range(10):
    if i % 3== 0 and i% 5 == 0:
        print("Nilaii", i, ': Mendesis dan mendengung')
    elif i % 3 == 0: 
        print("Nilaii", i, ': Mendesis')
    elif i % 5 == 0:
        print("Nilaii", i, ': Mendengung')
    else: print(i, '-')

#deklarasi variabel dengan tipe list
number_list = []
n = int(input("Input ukuran list: "))
jum = 0
print("\n")
for i in range(0, n):
    print("Input nilai pada indeks ke: ", 1, )
    list_item = int(input())
    jum = jum + list_item
    #menambahkan data ke variabel list
    number_list.append(list_item)
print("Data List", number_list)
print("Jumlah: ", jum)

#deklarasi varibel dengan tipe list
listA = []
n = int(input("Input ukuran list: "))
jum = 0
#print("\n")
for i in range(0, n):
    print("Input nilai pada indeks ke: ", i, )
    list_item = int(input())
    listA.append(list_item)

#konversi tipe List menjadi tipe Tuple
tupleA = tuple (listA)
jum = sum(tupleA)
print("Data Tuple A", tupleA)
print("Jumlah item pada Tuple A: ", jum)

#Deklarasi variabel dengan tipe Dictionary
transaction_data = {
"transaction_id": 1000001,
"source_country": "United Kingdom",
"target_country": "Italy",
"send_currency": "GBP",
"send_amount": 1000.00,
"target_currency": "EUR",
"fx_rate": 1.1648674,
"fee_pct": 0.50,
"platform": "mobile"
}
for key in transaction_data:
    print(key, ":", transaction_data[key])