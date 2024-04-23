def main(s):
    # 切り取る文字数を 1 から始めて大きくしていき
    # 文字数のごとに set を作成して存在するパターンをカウントする
    count_ = 0
    for i in range(len(s)):
        str_len = i + 1
        str_set = set()

        for j in range(len(s) - (str_len - 1)):
            str_ = s[j : j + str_len]
            str_set.add(str_)

        count_ += len(str_set)

    return count_


if __name__ == "__main__":
    s = input()

    print(main(s))
