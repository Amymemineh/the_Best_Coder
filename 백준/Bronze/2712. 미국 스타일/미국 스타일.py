n = int(input())
dict = {'kg':(2.2046, 'lb'), 
        'lb':(0.4536, 'kg'),
        'l':(0.2642, 'g'),
        'g':(3.7854, 'l')}

for _ in range(n):
  a, b = input().split()
  a = float(a)
  num = "{:.4f}".format(a*dict[b][0])
  print(num, dict[b][1], sep=' ')