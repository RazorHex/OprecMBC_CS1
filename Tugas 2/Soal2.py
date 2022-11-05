print('========= MENGHITUNG TOTAL BELANJA =========')
total = int(input('Masukkan Total Belanja : '))
member = input('Apakah Member (y/t): ')
if member == 'y': #diskon 5%
  diskon = 5
  if 500000 <= total < 1000000: #diskon 2%
    diskon = diskon + 2
    print('Selamat anda mendapatkan diskon\t: ' + str(diskon) + '%')
  elif total >= 1000000: #diskon 3%
    diskon = diskon + 3
    print('Selamat anda mendapatkan diskon\t: ' + str(diskon) + '%')
  else:
    print('Selamat anda mendapatkan diskon\t: ' + str(diskon) + '%')
else:
  print('Total belanja anda\t ' + str(total))