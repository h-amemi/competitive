def main(month_def, day_def, y, m, d, plus_day=1):
    # 割り算でオーバーした分を計算したいので、0 始まりである必要がある
    # 12 29 の次を 12 30 としたとき、30 // 30 は 1 になるので、1 はじまりは都合が悪い
    y -= 1
    m -= 1
    d -= 1

    d += plus_day
    m += d // day_def
    d = d % day_def
    y += m // month_def
    m = m % month_def
    print(y + 1, m + 1, d + 1)


if __name__ == "__main__":
    month_def, day_def = tuple([int(i) for i in (input().split())])
    y, m, d = tuple([int(i) for i in (input().split())])

    main(month_def, day_def, y, m, d, 1)
