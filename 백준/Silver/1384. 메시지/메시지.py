group = 0

while True:
  group += 1
  n = int(input())
  if n == 0: break
  name_list = []
  message_list = []

  for _ in range(n):
    name, *message = input().split()
    name_list.append(name)
    message_list.append(message)
  
  print(f'Group {group}')
  nasty = False
  for i in range(n):
    if 'N' in message_list[i]:
      for j in range(len(message_list[i])):
        if message_list[i][j] == 'N':
          print(f'{name_list[i-j-1]} was nasty about {name_list[i]}')
        nasty = True
  if not nasty: print('Nobody was nasty')
  print()