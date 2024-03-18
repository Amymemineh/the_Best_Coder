import itertools

n = int(input())
k = int(input())
n_list = list(int(input()) for _ in range(n))
num = set()

for i in itertools.permutations(n_list, k):
  num.add(''.join(map(str, i)))

print(len(num))