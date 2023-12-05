def solution(numbers, hand):
    
    l = [3,0]
    r = [3,2]
    key_pad = {1: [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 5: [1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], 0:[3,1]}
    
    result = ''
           
    for number in numbers: 
        if number == 1 or number == 4 or number == 7:
            l = key_pad[number]
            result+="L"
        elif number == 3 or number == 6 or number == 9:
            r = key_pad[number]
            result+="R"
        else:
            dl_x = abs(l[0] - key_pad[number][0])
            dl_y = abs(l[1] - key_pad[number][1])
            dr_x = abs(r[0] - key_pad[number][0])
            dr_y = abs(r[1] - key_pad[number][1])
            if dl_x + dl_y < dr_x + dr_y:
                l = key_pad[number]
                result+="L"
            elif dl_x + dl_y > dr_x + dr_y:
                r = key_pad[number]
                result+="R"
            elif dl_x + dl_y == dr_x + dr_y:
                if hand == "left":
                    l = key_pad[number]
                    result+="L"
                else :
                    r = key_pad[number]
                    result+="R"

    return result