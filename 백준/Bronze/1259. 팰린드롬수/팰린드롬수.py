while True:
  rom = input()
  if rom == '0': break
  else:
    rev_rom = rom[::-1]
    if rom == rev_rom:
      print("yes")
    else:
      print("no")
