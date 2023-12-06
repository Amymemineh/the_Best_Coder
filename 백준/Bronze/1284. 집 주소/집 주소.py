while True:
    n= input()
    answer = 0
    
    if n=="0":
        break
    else:
        for i in n:   
            if i == "1":
                answer+=2
            elif i == "0":
                answer+=4
            else:
                answer+=3
        answer+=(len(n)+1)        
        
    print(answer)