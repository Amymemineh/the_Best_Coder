from datetime import datetime

month = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
now = input().replace(',', '').replace(':', ' ').split() 

now_date = datetime(int(now[2]), month.index(now[0])+1, int(now[1]), int(now[3]), int(now[4]))
now_year = datetime(int(now[2]), 1, 1)
next_year = datetime(int(now[2])+1, 1, 1)

year = (next_year - now_year).total_seconds()
before = (now_date - now_year).total_seconds()

print(before / year * 100)