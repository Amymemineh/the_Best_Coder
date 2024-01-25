T=int(input())
for _ in range(T):
  space=input() #공백 잡아 먹는 애
  temp=[]
  n,m=map(int,input().split())
  #내림차순 정렬
  jun=sorted(list(map(int,input().split())),reverse=False)
  bi=sorted(list(map(int,input().split())),reverse=False)

  #pop은 뒤에서부터 빠짐
  while jun and bi:
    if jun[-1]>=bi[-1]:
      bi.pop()
    else:
      jun.pop()

  if jun:
    print('S')
  elif bi:
    print('B')
  else:
    print('C')