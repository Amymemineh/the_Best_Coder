n = int(input())
word = set(input() for _ in range(n))
result = sorted(list(word), key = lambda x : (len(x), x))
print("\n".join(result))