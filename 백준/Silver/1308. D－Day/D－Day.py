import datetime

now = input().split()
dd = input().split()

now_d = datetime.date(int(now[0]), int(now[1]), int(now[2]))
dd_d = datetime.date(int(dd[0]), int(dd[1]), int(dd[2]))

D_day = str(now_d - dd_d).split()[0]

if int(D_day) > - 365243 : print(f'D{D_day}')
else: print('gg')