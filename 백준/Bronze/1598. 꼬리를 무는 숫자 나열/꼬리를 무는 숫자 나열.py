a, b = map(int, input().split())

a_x = (a-1)//4
b_x = (b-1)//4
a_y = (a-1)%4
b_y = (b-1)%4

x = abs(a_x - b_x)
y = abs(a_y - b_y)

print(x+y)
