from collections import defaultdict

n, m = tuple(int(i) for i in input().split())
lines = [[int(i) - 1 for i in input().split()] for _ in range(m)]  # 人の番号は0はじまりにする


"""
負けがついた人にどんどんスコアを減らしていって、
最終的に全く負けがつかなかった(初期値から変動がない)ひとを探せばよい
また、一度も情報が出てこない人がいる or 同率一位がいる場合、-1
"""

score_dict = defaultdict(lambda: None)

for line in lines:
    a = line[0]
    b = line[1]
    if score_dict[a] is None:
        score_dict[a] = 0
    if score_dict[b] is None:
        score_dict[b] = 0

    score_dict[b] += 1

saikyos = []
for i in range(n):
    if score_dict[i] is None:
        print(-1)
        exit()
    if score_dict[i] == 0:
        saikyos.append(i)

print(saikyos[0] + 1 if len(saikyos) == 1 else -1)
