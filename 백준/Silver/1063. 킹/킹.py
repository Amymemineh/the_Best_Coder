dic = {"R":[1, 0], "L":[-1, 0], "B":[0, -1], "T":[0, 1], 
       "RT":[1, 1], "LT":[-1, 1], "RB":[1, -1], "LB":[-1, -1]}

king, stone, n = input().split()
king_x, king_y = ord(king[0]), int(king[1])
stone_x, stone_y = ord(stone[0]), int(stone[1])
n = int(n)

move = [input() for _ in range(n)]

for m in move:
  dx, dy = dic[m][0], dic[m][1]
  new_kx, new_ky = king_x + dx, king_y + dy
  if not(ord('A') <= new_kx <= ord('H') and 1 <= new_ky <= 8): continue
  if new_kx == stone_x and new_ky == stone_y:
    new_sx, new_sy = stone_x + dx, stone_y + dy
    if not(ord('A') <= new_sx <= ord('H') and 1 <= new_sy <= 8): continue
    stone_x, stone_y = new_sx, new_sy
  king_x, king_y = new_kx, new_ky

print(chr(king_x) + str(king_y))
print(chr(stone_x) + str(stone_y))