n = int(input())
room = [input() for _ in range(n)]

garo_noop = sum(1 for row in room for word in row.split('X') if len(word) >= 2)
sero_noop = sum(1 for col in zip(*room) for word in ''.join(col).split('X') if len(word) >= 2)

print(garo_noop, sero_noop)