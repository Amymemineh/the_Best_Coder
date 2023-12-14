cnt_list = []
for _ in range(9):
  cnt_list.append(int(input()))

max_num = max(cnt_list)
dict = {string: i for i, string in enumerate(cnt_list)}
print(max_num, dict[max_num]+1, sep = '\n')