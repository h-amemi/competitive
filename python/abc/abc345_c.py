from collections import defaultdict


def main(s):
    """
    - 文字種類ごとに、別文字と入れ替えられる数を足していく
    - aabcde なら
        - aa をひとまとめにして、
        - 入れ替えられる対象数 (bcde の 4 つ) × 重複数 (aa の 2) = 8
        - a を抜いたもので繰り返し...
    """
    len_ = len(s)

    dict_ = defaultdict(int)
    for char_ in s:
        dict_[char_] += 1

    kumiawase = 0
    has_dup = False

    for k, v in dict_.items():
        kumiawase += (len_ - v) * v

        len_ -= v
        has_dup = has_dup or (v >= 2)

    return kumiawase + (1 if has_dup else 0)


if __name__ == "__main__":
    s = input()

    print(main(s))
