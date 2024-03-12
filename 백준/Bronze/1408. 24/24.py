now = list(map(int, input().split(":")))
start = list(map(int, input().split(":")))

now_s = now[0]*3600 + now[1]*60 + now[2]
start_s = start[0]*3600 + start[1]*60 + start[2]

result = start_s - now_s
if result < 0:
  result += 24*3600

h = result//3600
m = (result%3600)//60
s = (result%3600)%60

print(f'{h:02}:{m:02}:{s:02}')