A, B = input().split()

a = sum([int(i) for i in A])
b = [int(j) for j in B]

answer = 0

for bb in b:
  answer += a * bb

print(answer)