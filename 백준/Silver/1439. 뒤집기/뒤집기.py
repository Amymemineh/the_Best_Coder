s = input()

one = s.count("1")
zero = len(s) - one

z_idx = [i for i, char in enumerate(s) if char == "0"]
o_idx = [i for i, char in enumerate(s) if char == "1"]

z_cnt = 0
o_cnt = 0

if z_idx:
    for i in range(len(z_idx) - 1):
        if z_idx[i + 1] != z_idx[i] + 1:
            z_cnt += 1
    z_cnt += 1 

if o_idx:
    for i in range(len(o_idx) - 1):
        if o_idx[i + 1] != o_idx[i] + 1:
            o_cnt += 1
    o_cnt += 1 

print(min(z_cnt, o_cnt))
