#Surya Nathaniel Kattu
#Nim: 71160108
#Soal No 3

db = str(input("Masukkan daftar belanja anda : "))
print("Daftar Belanja", [db])

tdb = str(input("Masukkan barang yang ingin ditambahkan : "))

#percabangan
if tdb == db:
    print("Barang", tdb.upper(), "sudah berada dalam daftar belanja")
else: 
    print("Hasil penambahan pada daftar belanja : ", [db.capitalize(), tdb.upper()])