import itertools

N, A, B = tuple([int(i) for i in input().split()])


def get_keta_sum(n):
    sum_keta = 0
    for i in itertools.count(start=0):
        sum_keta += (n % (10 ** (i + 1))) // (10 ** i)
        if 0 == n // (10 ** (i + 1)):
            break
    return sum_keta


sum_i = 0
for i in range(1, N + 1):
    if A <= get_keta_sum(i) <= B:
        sum_i += i

print(sum_i)
