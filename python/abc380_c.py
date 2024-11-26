def main(n, k, s):
    # k - 1 番目の 1 の塊の後の 0 の塊と、k 番目の 1 の塊の位置を入れ替える
    katamari_of_1_count = 0
    current_index = 0

    # k - 1 番目の塊まで、カウントしながらすすめる
    while katamari_of_1_count < k - 1:
        katamari_type, current_index = get_katamari_only_index(s, current_index)
        if katamari_type == "1":
            katamari_of_1_count += 1

    # k - 1 番目の 1 の塊の後の 0 の塊
    _, katamari_0_end_index = get_katamari_only_index(s, current_index)
    # k 番目の 1 の塊
    _, katamari_k_end_index = get_katamari_only_index(s, katamari_0_end_index)

    return "".join(
        [
            s[:current_index],
            s[katamari_0_end_index:katamari_k_end_index],
            s[current_index:katamari_0_end_index],
            s[katamari_k_end_index:],
        ]
    )


def get_katamari_only_index(s, start_index):
    katamari_type = s[start_index]
    for i in range(start_index + 1, len(s)):
        if not s[i] == katamari_type:
            # katamari_type と違った index を返す (次の塊の先頭)
            return katamari_type, i
    return katamari_type, len(s)


def get_katamari(s):
    # 当初、文字列を分割して最後にまとめるロジックとしていたが TLE になったので、
    # 要所のインデックスだけ取得して最後に文字列を生成するロジックに切り替えた
    katamari_type = s[0]
    for i in range(1, len(s)):
        if not s[i] == katamari_type:
            return katamari_type, s[:i], s[i:]
    return katamari_type, s, ""


if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input()

    print(main(n, k, s))
