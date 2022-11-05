print('========= SERAGAM TELKOM UNIVERSITY =========')
hari = input('Masukkan hari: ')
if(hari == 'senin'):
  print('Seragam anda hari ini merah')
elif (hari == 'selasa') or (hari == 'rabu'):
  print('Seragam anda hari ini putih')
elif (hari == 'kamis') or (hari == 'sabtu'):
  print('Seragam anda hari ini bebas')
elif (hari == 'jumat'):
  print('Seragam anda hari ini batik')
else:
  print('Hari yang anda input tidak tersedia')