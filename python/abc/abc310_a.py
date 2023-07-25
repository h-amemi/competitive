N, P, Q = tuple(int(i) for i in input().split())
Ds = [int(i) for i in input().split()]

waribiki = P - Q
min_d = min(Ds)

print(P if waribiki <= min_d else Q + min_d)
