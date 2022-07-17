N, A, B = tuple([int(i) for i in input().split()])
sum = 0
for i in range(1, N + 1):
    keta_10000 = i // 10000
    keta_1000 = i % 10000 // 1000
    keta_100 = i % 1000 // 100
    keta_10 = i % 100 // 10
    keta_1 = i % 10
    if A <= keta_10000 + keta_1000 + keta_100 + keta_10 + keta_1 <= B:
        sum += i

print(sum)
