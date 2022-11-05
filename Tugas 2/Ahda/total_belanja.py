total = int(input('Total Belanja\t: ').replace('.', ''))
member = input('Apakah member (y/t)\t: ')[0].lower()

if member == 'y':
  # diskon 5%
  dis = 5
  if 500000 <= total < 1000000:
    # diskon 2%
    dis = dis + 2
    print('Diskon anda\t: ' + str(dis) + '%')
  elif total >= 1000000:
    #diskon 3%
    dis = dis + 3
    print('Diskon anda\t: ' + str(dis) + '%')
  else:
    print('Diskon anda\t: ' + str(dis) + '%')

else:
  print('Total belanja anda\t: ' + str(total))
