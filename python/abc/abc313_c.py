n = int(input())
a_s = [int(i) for i in input().split()]

sorted_a_s = sorted(a_s)

# 最終系を作る
# 3 4 7 7 なら
# 5 5 5 6
sum_ = sum(sorted_a_s)
saishukei = [sum_ // n for i in range(n)]
for i in range(sum_ % n):
    saishukei[n - 1 - i] += 1

count = 0

for i in range(n):
    count += abs(sorted_a_s[i] - saishukei[i])

print(count // 2)
