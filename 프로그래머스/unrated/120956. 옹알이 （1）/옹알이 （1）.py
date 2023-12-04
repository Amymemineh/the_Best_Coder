def solution(babbling):
    
    says = ["aya", "ye", "woo", "ma"]
    result = 0
    
    for i in range(len(babbling)):
        
        for say in says:
            if say in babbling[i]:
                babbling[i] = babbling[i].replace(say, "*")
    
        if all(char == "*" for char in babbling[i]):
            result += 1

    return result