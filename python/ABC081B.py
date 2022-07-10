def how_many_2_in_factor(i):
    """因数分解したときに2がいくつ入ってるか"""
    if i == 0:
        return 0
    if i % 2 != 0:
        return 0
    return how_many_2_in_factor(i / 2) + 1


n = int(input())
a_list = [int(x) for x in input().split()]
# それぞれ、何回2で割れるかの回数を計算し、一番少ない回数を保持し、最後に出力する
c = None
for i, a in enumerate(a_list):
    count_2_in_factor = how_many_2_in_factor(a)
    if i == 0:
        c = count_2_in_factor
    if count_2_in_factor < c:
        c = count_2_in_factor
print(c)
