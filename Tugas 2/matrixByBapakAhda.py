n = int(input("Masukkan Angka = "))


for i in range(n):
    # print('i = ', i)
    temp = []
    for j in range(n):
        print('j = ', j)
        temp.append("*")
    print("".join(temp))