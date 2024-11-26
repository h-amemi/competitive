def main(n, values):
    # -N から 2N まで数字の列だと考える
    # L = 1, R = 2, N = 6 のとき、L を 4 に移動させるときは
    # L (1) から、4 - N (6) まで移動することが操作回数であるとする
    # 1 と - 2 の距離なので、1 - (-2) = 3 回の操作が必要

    l, r = 1, 2
    count = 0
    for hand, to in values:
        if hand == "L":
            count += ido(n, l, to, r)
            l = to
        else:
            count += ido(n, r, to, l)
            r = to

    return count


def ido(n, now, to, another_hand):
    if (
        (now <= to <= another_hand)
        or (another_hand <= to <= now)
        or (to <= now <= another_hand)
        or (another_hand <= now <= to)
    ):
        return abs(now - to)
    elif now < another_hand < to:
        return abs(now - (to - n))
    else:  # to < another_hand < now:
        return abs(now - (to + n))


if __name__ == "__main__":
    n, q = map(int, input().split())

    values = [(a, int(b)) for a, b in (input().split() for _ in range(q))]

    print(main(n, values))
