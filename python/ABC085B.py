N = int(input())
d_s = [int(input()) for _ in range(N)]

latest = None
dup_count = 0
for i in sorted(d_s):
    if i == latest:
        dup_count += 1
    latest = i

print(len(d_s) - dup_count)
