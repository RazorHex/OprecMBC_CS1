import os # module for accessing operating system

besar = int(input('Masukan nilai n\t: '))
matriks_1 = [ for jum in range(besar)] # row
matriks_2 = [jum for jum in range(besar)] # column

os.system('cls')
print('Nilai n\t: ', besar)

for i in matriks_1: # selecting the row
  temp = []
  for j in matriks_2: # filling the column
    if i == 0 or i == len(matriks_1) - 1:
      temp.append('*')
    elif j == 0 or j == len(matriks_2) - 1:
      temp.append('*')
    else:
      temp.append('#')
  print(''.join(temp))