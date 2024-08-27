def main(x):
    # https://docs.python.org/ja/3/library/stdtypes.html#printf-style-string-formatting
    # 'g' 浮動小数点数。指数部が -4 以上または精度以下の場合には小文字指数表記、それ以外の場合には10進表記。
    return "%g" % float(x)


if __name__ == "__main__":
    x = input()

    print(main(x))
