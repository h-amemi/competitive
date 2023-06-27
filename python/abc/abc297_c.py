h, w = tuple(int(i) for i in input().split())
s_s = [input() for _ in range(h)]

for s in s_s:
    is_last_t = False
    for i, chara in enumerate(s):
        if chara == "T":
            if is_last_t:
                s = s[: i - 1] + "PC" + s[i + 1 :]
                is_last_t = False
            else:
                is_last_t = True
        else:
            is_last_t = False
    print(s)
