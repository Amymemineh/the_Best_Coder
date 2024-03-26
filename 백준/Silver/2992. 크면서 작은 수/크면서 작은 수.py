from itertools import permutations

x = input()
num_set = set(''.join(num) for num in permutations(x))
answer = [new for new in num_set if new > x]

print(0) if not answer else print(min(answer))