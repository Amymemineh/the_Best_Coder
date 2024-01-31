dna = {"AA": "A", "AG": "C", "AC": "A", "AT": "G",
       "GG": "G", "CG": "T", "GT": "A",
       "CC": "C", "CT": "G",
       "TT": "T"}

n = int(input())
yum = list(input())

for i in range(1, n):
  result = dna["".join(sorted(yum[-2:]))]
  yum.pop()
  yum.pop()
  yum.append(result)

print(yum[0])