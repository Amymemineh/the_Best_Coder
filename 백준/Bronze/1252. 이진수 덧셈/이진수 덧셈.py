a, b = input().split()
aa = int(a, 2)
bb = int(b, 2)

answer = bin(aa+bb)
print(answer[2:])