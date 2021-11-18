#Surya Nathaniel Kattu
#Nim: 71160108
#Soal No 2

na = float(input("Nilai a : "))
nb = float(input("Nilai b : "))
nc = float(input("Nilai c : "))

D = (nb**2) - (4*na*nc) #rumus diskriminan

a1 = (-nb+D)/(2*na) #akar 1
a2 = (-nb-D)/(2*na) #akar 2

#percabangan
if D < 0:
    print("Fungsi tersebut tidak memiliki angka riil")
elif D > 0:
    print("Akar - akar dari persamaan tersebut adalah", a1, "dan", a2)
elif D == 0:
    print("Fungsi tersebut memiliki akar kembar yaitu ", a2)    