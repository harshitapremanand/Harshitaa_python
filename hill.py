n = int(input('Enter the number of rows: '))
rows = n +1
r = rows

for a in range(1, rows, 1):
      for b in range(a, rows, 1):
            print(" ", end= '  ')
      for d in range(1, (2 *a + 1) - 1, 1):
             print("*", end='  ')
      print()

for i in range(1, r, 1):
    for j in range(1, i+1, 1):
          print(" ", end= '  ')
    for k in range(i, rows, 1):
          print("*", end = '  ')
    for l in range(i, rows-1, 1 ):
          print("*", end = '  ')
    print()
