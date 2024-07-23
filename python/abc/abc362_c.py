def main(n, values):
    # L 側の合計が 0 より大きい場合は条件を満たせず
    # R 側の合計が 0 より小さい場合も条件を満たせない
    # そうでない場合には条件を満たす数列が存在する
    sum_l = sum(value[0] for value in values)
    sum_r = sum(value[1] for value in values)

    if 0 < sum_l or sum_r < 0:
        return None

    ret = [value[0] for value in values]

    # L をベースに数列を作成する
    # sum_l がマイナスなので、それを 0 に近づけていく (プラスする)
    # 各項目について R の数までしかプラスできないので、プラスできるのは R - L まで
    for i in range(n):
        plus_ = min(values[i][1] - values[i][0], -sum_l)
        sum_l += plus_
        ret[i] += plus_

    return ret


if __name__ == "__main__":
    # n
    n = int(input())

    # int list
    values = [[int(i) for i in (input().split())] for _ in range(n)]

    answer = main(n, values)
    if not answer:
        print("No")
    else:
        print("Yes")
        print(*answer)
