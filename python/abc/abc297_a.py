n, d = tuple(int(i) for i in input().split())
t_s = [int(i) for i in input().split()]

doubleclicked = -1
last_t = t_s[0]
for t in t_s[1:]:
    if t - last_t <= d:
        doubleclicked = t
        break
    last_t = t
print(doubleclicked)
