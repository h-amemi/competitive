def ceil_device_10(x):
    """
    - 桁数的に、double だと足りないので工夫する必要がある
    - 1/10 するまえに細工したい
    - 1 桁目を切り上げしておく
        - 1 桁目が 0 以外の場合 + 10 する
    - マイナスの場合
        - -13
        - -1.3
        - -1.3 以上の整数で一番小さいのは -1
        - なので、10の桁を繰り上げればいいだけじゃない
        - マイナスの場合をケアする
    """
    x_str = str(x)
    if x < 0:
        return int(x_str[0:-1] if len(x_str) >= 3 else "0")

    ret = int(x_str[0:-1] if len(x_str) >= 2 else "0")
    x_str_1 = x_str[-1]
    if not x_str_1 == "0":
        ret += 1

    return ret


if __name__ == "__main__":
    x = int(input())

    print(ceil_device_10(x))
