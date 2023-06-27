a, b = tuple(int(i) for i in input().split())

# 愚直にやると TLE
# count_ = 0
# while not a == b:
#     delta_abs = abs(a - b)
#     if a > b:
#         a = delta_abs
#     else:
#         b = delta_abs
#     count_ += 1
# print(count_)

if a >= b:
    max_, min_ = a, b
else:
    max_, min_ = b, a

count_ = 0

while True:
    count_ += max_ // min_
    mod = max_ % min_

    if mod == 0:
        break

    max_ = min_
    min_ = mod

print(count_ - 1)
