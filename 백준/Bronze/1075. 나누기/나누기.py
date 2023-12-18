N = input()
F = int(input())
list_N = []

min_N = int(N[:-2]+'00')
max_N = int(N[:-2]+'99')

for i in range(min_N, max_N+1):
    if i%F == 0:
        list_N.append(i)
    else: pass

two = str(min(list_N))[-2:]
print((two))