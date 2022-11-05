data = {
  'senin' : 'putih',
  'selasa' : 'merah',
  'rabu' : 'merah',
  'kamis' : 'bebas',
  'jumat' : 'batik',
  'sabtu' : 'bebas'
}

hari = input('Masukan hari\t: ')

# note:
#  try akan mencoba untuk menjalankan program kalau ada error yang akan di jalankan adalah program dalam except
try:
  val = data.get(hari)
  print('Seragam ' + hari + '\t: ' + val)
except:
  print('Seragam tidak ditemukan')