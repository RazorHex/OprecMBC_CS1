hari = input("Masukkan Hari : ")
hari = hari.lower()

def seragam():
    if hari == "senin":
        print("Seragam anda hari ini Merah")
    elif hari == "selasa" or hari == "rabu":
        print("Seragam anda hari ini Putih")
    elif hari == "jumat":
        print("Seragam anda hari ini Batik")
    elif hari == "kamis" or hari == "sabtu" :
        print("Seragam anda hari ini BEBAS")
    else :
        print("Ga usah pake Seragam, nape sih ribet banget")
        
seragam()
