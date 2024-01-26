for i in range(int(input()), -1, -1):
  if all(num in ['4', '7'] for num in str(i)):
    print(i)
    break