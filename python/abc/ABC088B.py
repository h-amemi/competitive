N = int(input())
a_s = [int(a) for a in input().split()]

alice_score = 0
bob_score = 0
for i, a in enumerate(sorted(a_s, reverse=True)):
    if i % 2 == 0:
        alice_score += a
    else:
        bob_score += a

print(alice_score - bob_score)
