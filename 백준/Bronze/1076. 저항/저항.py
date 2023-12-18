dict_color = {"black":(0,1), "brown": (1,10), "red": (2,100), "orange": (3,1000), "yellow": (4,10000), "green": (5,100000), "blue": (6,1000000), "violet": (7,10000000), "grey": (8,100000000), "white": (9,1000000000)}

a = dict_color[input()][0]
b = dict_color[input()][0]
c = dict_color[input()][1]

answer = int(str(a)+str(b))*c
print(answer)