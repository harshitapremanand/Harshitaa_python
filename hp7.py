n = int(input('Enter the number of rows: '))
rows = n+1

print("increasing starred triangle")
for i in range(0, rows, 1):
      for j in range(1, i+1, 1):
              print("* ", end = ' ')
      print()


print("decreasing starred triangle")
for k in range(0, rows, 1):
      for l in range(k, rows, 1):
              print("* ", end = ' ')
      print()

print("Mirror image increasing starred pattern:")
for a in range(0, rows, 1)

