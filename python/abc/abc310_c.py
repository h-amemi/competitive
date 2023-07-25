n = int(input())
s_s = [input() for _ in range(n)]

polls = set()

for s in s_s:
    if s in polls or s[::-1] in polls:
        continue
    else:
        polls.add(s)

print(len(polls))
