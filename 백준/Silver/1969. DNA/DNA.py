n, m = map(int, input().split())
dna = [input() for _ in range(n)]
result = ''
ham_distance = 0


for i in range(m):
  dna_dic = {"A":0, "T":0, "G":0, "C":0}  
  for j in range(n):
    dna_dic[dna[j][i]] += 1
    
  ham = max(dna_dic.values())
  answer = sorted([key for key, value in dna_dic.items() if value == ham])
  result += answer[0]
  ham_distance += n - ham 

print(result, ham_distance, sep = '\n')
    