import os

n = int(input("Masukkan Range Angka Ganjil : "))
os.system("cls")

def ganjil():
    for i in range(0, n):
        if i % 2 != 0 :
            print(i)   
            
print("Print Angka Ganjil di range 0 sampai ",n)
ganjil()


# Algoritma :
# Bilangan Ganjil
#  n % 2 != 0 
#  Input = n
#  fungsi ganjil, pengulangan for i dengan batas range sampai dengan n. Awalan 0. 
# Jika i modulus 2 tidak sama dengan 0, print(i, end=" ")
# Jika ku isi 5, dia akan ngecek dari angka 0 hingga angka 5 (***Sebelum 5 = 4)
# Output = 1,3