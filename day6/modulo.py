days = 8

for day in range(days):
    print('day: %d' % day)
    print('i1: %d' % ((day + 7) % 9))
    print('i2: %d\n' % (day % 9) )