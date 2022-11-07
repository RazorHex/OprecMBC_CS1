import os

n = int(input("Jumlah Total Belanja = "))
member = input("Apakah member (y/t) = ")

def belanja():
    if n > 1000000:
        if member == "y" :
            print("Selamat anda mendapatkan diskon 8%")
        else:
            print("Selamat anda mendapatkan diskon 3%")
    else :
        if member == "y" :
            print("Selamat anda mendapatkan diskon 7%")
        else:
            print("Selamat anda mendapatkan diskon 2%")
            
os.system("cls")

belanja()


# *** NOTe :
# if member atau tidak member dan if total belanja 500k <= x <=1jt = diskon 2% else