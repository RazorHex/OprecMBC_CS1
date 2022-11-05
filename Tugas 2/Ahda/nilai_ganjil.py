import os

angka = int(input('Masukan nilai n\t: '))
os.system('cls')

print('Finding odd number between 0 and ' + str(angka) + '....')

for i in range(angka):
  if i % 2 != 0:
    print(i)