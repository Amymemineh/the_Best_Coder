bird = int(input())
song = 1
cnt = 0

while bird > 0:
  bird -= song 
  song += 1    
  cnt += 1
  if bird < song:
    song = 1

print(cnt)