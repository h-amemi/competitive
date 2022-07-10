def usable_coins(x, coins, val):
    mod = x // val
    return mod if mod < coins else coins


def main():
    coins_500 = int(input())
    coins_100 = int(input())
    coins_50 = int(input())
    x = int(input())

    c = 0
    # まず、最適な枚数を計算して、そこからどれだけ小さいコインで置き換えられるかを計算していく
    usable_500 = usable_coins(x, coins_500, 500)
    # print("usable_500: {}".format(usable_500))
    for i_500 in reversed(range(usable_500 + 1)):  # 大きい方から減らしていく
        # print("i_500: {}".format(i_500))
        usable_100 = usable_coins(x - 500 * i_500, coins_100, 100)
        # print("usable_100: {}".format(usable_100))
        for i_100 in reversed(range(usable_100 + 1)):
            # print("i_100: {}".format(i_100))
            usable_50 = usable_coins(x - (500 * i_500 + 100 * i_100), coins_50, 50)
            # print("usable_50: {}".format(usable_50))
            if x == (500 * i_500 + 100 * i_100 + 50 * usable_50):
                c += 1
                continue
            break

    print(c)


if __name__ == "__main__":
    main()
