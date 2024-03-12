x, y = input().split()

rev_x = x[::-1]
rev_y = y[::-1]

sum = int(str(int(rev_x) + int(rev_y))[::-1])

print(sum)