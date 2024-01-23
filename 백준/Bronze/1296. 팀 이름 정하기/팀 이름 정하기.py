name = input()
team = [input() for i in range(int(input()))]
team.sort()

win = {}

for t in team:
    l = name.count("L") + t.count("L")
    o = name.count("O") + t.count("O")
    v = name.count("V") + t.count("V")
    e = name.count("E") + t.count("E")
    per = ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e)) % 100
    win[t] = per


print(max(win, key=win.get))