n = int(input())
num_list = list(map(int, input().split()))
num_dict = {}

for num in num_list:
  if num in num_dict:
    num_dict[num] += 1
  else:
    num_dict[num] =  1

max_num = 0
for key, value in num_dict.items():
  if key == value and key >= max_num :
    max_num = key

if max_num == 0 and 0 in num_dict:
  print(-1)
else:
  print(max_num)