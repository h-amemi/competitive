def main(n, values):
    # values[i] が何人目 (1はじまり) の人の後ろにいるかの list がある
    # "何人目の後ろか" が key, "自分が何人目か" が value の辞書を作って引いていけばいい

    # value - 1 することで、0 はじまりの index にする
    dareno_ushiro_dict = {value - 1: i for i, value in enumerate(values)}

    dare_no_ushiro = -2
    junban = []
    while len(junban) < n:
        dare_position = dareno_ushiro_dict[dare_no_ushiro]
        junban.append(str(dare_position + 1))
        dare_no_ushiro = dare_position

    return junban


if __name__ == "__main__":
    n = int(input())
    values = [int(i) for i in (input().split())]

    print(" ".join(main(n, values)))
