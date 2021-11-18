#Surya Nathaniel Kattu
#Nim: 71160108
#Soal No 4

blg1 = int(input("Masukkan bilangan 1 : "))
blg2 = int(input("Masukkan bilangan 2 : "))
blg3 = int(input("Masukkan bilangan 3 : "))

#percabangan yang panjang sekali
if blg1 > blg2 > blg3:
    print("Urutan bilangan dari yang terbesar adalah ", blg1, blg2, blg3)
elif blg1 > blg3 > blg2:
    print("Urutan bilangan dari yang terbesar adalah ", blg1, blg3, blg3)
elif blg1 == blg2 > blg3:
    print("Urutan bilangan dari yang terbesar adalah ", blg1, blg2, blg3)  
elif blg1 == blg3 > blg2:
    print("Urutan bilangan dari yang terbesar adalah ", blg1, blg3, blg2)
#batas biar rapih
elif blg2 > blg1 > blg3:
    print("Urutan bilangan dari yang terbesar adalah ", blg2, blg1, blg3)
elif blg2 > blg3 > blg1:
    print("Urutan bilangan dari yang terbesar adalah ", blg2, blg3, blg1)
elif blg2 == blg1 > blg3:
    print("Urutan bilangan dari yang terbesar adalah ", blg2, blg1, blg3)  
elif blg2 == blg3 > blg1:
    print("Urutan bilangan dari yang terbesar adalah ", blg2, blg3, blg1)    
#batas biar rapih
elif blg3 > blg1 > blg2:
    print("Urutan bilangan dari yang terbesar adalah ", blg3, blg1, blg2)
elif blg3 > blg2 > blg1:
    print("Urutan bilangan dari yang terbesar adalah ", blg3, blg2, blg1)
elif blg3 == blg2 > blg1:
    print("Urutan bilangan dari yang terbesar adalah ", blg3, blg2, blg1)  
elif blg3 == blg1 > blg2:
    print("Urutan bilangan dari yang terbesar adalah ", blg3, blg1, blg2)                       