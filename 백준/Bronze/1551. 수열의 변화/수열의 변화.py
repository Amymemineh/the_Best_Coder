n, k = map(int, input().split())
num = list(map(int, input().split(",")))
new = num.copy()

for _ in range(k):
    new = [new[i + 1] - new[i] for i in range(len(new) - 1)]

print(",".join(map(str, new)))