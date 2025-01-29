import itertools


def main(h, w, d, grid_lines):
    # すべての床マスの組み合わせに対して、そこに加湿器を設置した場合に、加湿できる床のマス数を算出する

    zahyos = [(i, j) for i in range(h) for j in range(w)]

    humidified_points = {}
    for i in range(h):
        for j in range(w):
            humidified_points[(i, j)] = humidified_point(i, j, d, grid_lines)

    max_humidified = 0
    for zahyo_1, zahyo_2 in itertools.combinations(zahyos, 2):
        humidified_set_1 = humidified_points[zahyo_1]
        humidified_set_2 = humidified_points[zahyo_2]

        humidified = len(humidified_set_1 | humidified_set_2)
        if humidified > max_humidified:
            max_humidified = humidified

    return max_humidified


def humidified_point(i, j, d, grid_lines):
    humidified = set()
    point = grid_lines[i][j]
    if not point == ".":
        return humidified
    # マンハッタン距離 d 以内のマスの床の数をカウントする
    # 現在の行
    humidified = humidified.union(humidified_in_line(i, j, d, grid_lines))

    # 上下
    for k in range(d):
        tate = k + 1
        yoko_range = d - tate

        # 上方向
        if 0 <= i - tate <= h - 1:  # 行が存在する場合
            humidified = humidified.union(
                humidified_in_line(i - tate, j, yoko_range, grid_lines)
            )

        # 下方向
        if 0 <= i + tate <= h - 1:  # 行が存在する場合
            humidified = humidified.union(
                humidified_in_line(i + tate, j, yoko_range, grid_lines)
            )

    return humidified


def humidified_in_line(i, j, d, grid_lines):
    humidified = set()
    # 直下
    if grid_lines[i][j] == ".":
        humidified.add((i, j))
    for l in range(d):
        yoko = l + 1
        if 0 <= j - yoko <= w - 1:  # yoko 左側の列が存在する場合
            if grid_lines[i][j - yoko] == ".":
                humidified.add((i, j - yoko))
        if 0 <= j + yoko <= w - 1:  # yoko 右側の列が存在する場合
            if grid_lines[i][j + yoko] == ".":
                humidified.add((i, j + yoko))
    return humidified


if __name__ == "__main__":
    h, w, d = map(int, input().split())
    grid_lines = [input() for _ in range(h)]

    print(main(h, w, d, grid_lines))
