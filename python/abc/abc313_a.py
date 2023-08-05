N = int(input())
P_S = [int(i) for i in input().split()]

if N == 1:
    print(0)
else:
    max_ = max(P_S[1:])

    print(0 if max_ < P_S[0] else max_ - P_S[0] + 1)
