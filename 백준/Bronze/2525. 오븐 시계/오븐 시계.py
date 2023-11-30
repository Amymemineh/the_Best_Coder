H, M=map(int, input().split())
T=int(input())
M+=H*60+T
H=M//60
M=M%60

if H>=24:
   H-=24
        
print(H,M)