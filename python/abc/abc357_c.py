def main(n):
    return [
        ["." if is_white(x, y, n) else "#" for y in range(3**n)] for x in range(3**n)
    ]


def is_white(x, y, n):
    if x % 3 == 1 and y % 3 == 1:
        # 最小の9分割の中で真ん中の座標であれば白
        return True
    if n >= 2:
        # 1階層大きな9分割とみなして再帰的に判定する
        # (n が 1 の場合はこの条件に入らない)
        return is_white(x // 3, y // 3, n - 1)
    return False


if __name__ == "__main__":
    n = int(input())

    grid = main(n)
    [print("".join(row)) for row in grid]
