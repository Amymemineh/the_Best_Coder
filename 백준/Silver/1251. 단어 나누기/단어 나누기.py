word = input()
hubo = set()

for i in range(1, len(word) - 1):
    for j in range(i+1, len(word)):
        hubo.add(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])

print(min(hubo))