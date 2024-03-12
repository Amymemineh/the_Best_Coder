multi, min = map(int, input().split())
for num in range(2,min):
    if multi%num == 0:
        print("BAD", num)
        break

else: 
    print("GOOD")