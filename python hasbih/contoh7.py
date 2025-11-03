list1 = ['Doni Kusuma', 'Anton Wijaya', 'Kimia', 1997, 2020]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d", "e"]
#elemen baru pada list 2
list2_new = ["Chandra Gumelar", "Arshanty"]
list3_new = [20, 30, 40]
list2.append(list2_new)
list3.append(list3_new)
print ("Update isi List2", list2)
print ("Update isi List3", list3)
print ("Update isi List3 [5]: ", list3[5])

list1= ['Doni Kusuma', 'Anton Wijaya', 'Kimia', 1997, 2020]
list2 [1, 2, 3, 4, 5]
list3 ["a", "b", "c", "d", "e"]
#menghapus elemen pada list
del list2[2]
del list3[3]
print ("isi List2", list2)
print ("isi List3", list3)

list1= ['Doni Kusuma', 'Anton Wijaya', 'Kimia', 1997, 2020]
list2 [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d", "e"]
#menghapus elemen pada list
list2.remove (3)
list3.remove("c")
print ("isi List2", list2)
print ("isi List3", list3)

list1 = ['Doni Kusuma', 'Anton Wijaya', 'Kimia', 1997, 2020]
list2 [1, 2, 3, 4, 5]
list3= ["a", "b", "c", "d", "e"]
#menghapus elemen pada list
list2.pop(3)
list3.pop()
print ("isi List2", list2)
print ("isi List3", list3)

list1 = ['Doni Kusuma', 'Anton Wijaya', 'Kimia', 1997, 2020]
list2 [1, 2, 3, 4, 5]
list3 ["a", "b", "c", "d", "e"]
#menghapus elemen pada list
list2.clear()
list3.clear()
print ("isi List2", list2)
print ("isi List3", list3)

list1= ['Doni Kusuma', 'Anton Wijaya', 'Kimia', 'Zakaria']
list2 [1, 3, 5, 4, 2]
#mengurutkan elemen pada list
list1.sort()
list2.sort()
print ("isi List2", list1)
print ("isi List3", list2)

list1= ['Anton Wijaya', 'Doni Kusuma', 'Kimia', 'Zakaria']
list2 [1, 2, 3, 4, 5]
#membalikan urutan pada elemen pada list
list1.reverse()
list2.reverse()
print ("isi List2 : ", list1)
print ("isi List3 : ", list2)

list1= ['Doni Kusuma', 'Anton Wijaya', 'Kimia', 1997, 2020]
list2 [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d", "e"]
#menghitung panjang list
print ("Panjang list1: ", len(list1))
print ("Panjang list3", len(list3))
print ("Total Isi list2", sum(list2))

#semua elemen di list bernilai true
list1= [0, 1, 3, 4]
x = any(list1)
print (x)
#semua elemen di list bernilai false
list1 [0, False]
y = any(list1)
print (y)
#beberapa elemen di list bernilai true,
#jika elemen lain bernilai false
list1= [0, False, 5]
y = any(list1)
print (y)