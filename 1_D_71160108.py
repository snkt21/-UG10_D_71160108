#Surya Nathaniel Kattu
#Nim: 71160108
#Soal No 1

hm = int(input("Harga makanan sebesar RP "))
hs = int(input("Harga snack sebesar RP "))
hn = int(input("Harga minuman sebesar RP "))
ug = int(input("Uang yang anda bawa sebesar RP "))

ttl = hm+hs+hn
print("Total yang harus anda bayar sebesar RP ", ttl)

kl = abs(ttl - ug) #abs untuk nilai absolute 

#percabangan
if ttl < ug:
    print("Anda memiliki kembalian sebesar RP ", kl)
elif ttl > ug:
    print("Uang anda kurang! Anda memiliki utang sebesar RP ", kl)
else:
    print("Uang anda pas! Tidak ada kembalian dan utang :D ")     