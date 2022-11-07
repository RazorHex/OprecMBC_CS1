total = input('Total Belanja\t: ')

while not total.replace('.','').isdigit() or not len(total) > 5:
  total = input('Total Belanja\t: ')

member = input('Apakah member (y/n)\t: ')[0].lower()

if member == 'y':
  num = int(total.replace('.', ''))
  # diskon 5%
  dis = 5
  if 500000 <= num < 1000000:
    # diskon 2%
    dis = dis + 2
    print('Diskon anda\t: ' + str(dis) + '%')
    print('Total anda\t: ', num - (num * dis / 100))
  elif num >= 1000000:
    #diskon 3%
    dis = dis + 3
    print('Diskon anda\t: ' + str(dis) + '%')
    print('Total anda\t: ', num - (num * dis / 100))
  else:
    print('Diskon anda\t: ' + str(dis) + '%')
    print('Total anda\t: ', num - (num * dis / 100))

elif member == 'n':
  num = int(total.replace('.', ''))
  if 500000 <= num < 1000000:
    # diskon 2%
    dis = 2
    print('Diskon anda\t: ' + str(dis) + '%')
    print('Total anda\t: ', num - (num * dis / 100))
  elif num >= 1000000:
    #diskon 3%
    dis = 3
    print('Diskon anda\t: ' + str(dis) + '%')
    print('Total anda\t: ', num - (num * dis / 100))
  else:
    print('Total belanja anda\t: ' + total)

else:
  print('Error: wrong member variable')
