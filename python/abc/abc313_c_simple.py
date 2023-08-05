n = int(input())
a_s = [int(i) for i in input().split()]

"""
愚直にやってみる

sort して、min と max を同行する以外にも、
min の隣、max の隣 との間隔分についてはスキップできるのでそれでやる？
"""

count_ = 0

sorted_a_s = sorted(a_s)
min_ = sorted_a_s[0]
max_ = sorted_a_s[-1]
if max_ - min_ <= 1:
    print(count_)
    exit()
sorted_a_s[0] += 1
sorted_a_s[-1] -= 1
count_ += 1

while True:
    sorted_a_s = sorted(sorted_a_s)
    min_ = sorted_a_s[0]
    max_ = sorted_a_s[-1]
    if max_ - min_ <= 1:
        print(count_)
        exit()
    sorted_a_s[0] += 1
    sorted_a_s[-1] -= 1
    count_ += 1
