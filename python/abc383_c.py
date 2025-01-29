def main(h, w, d, grid_lines):
    # H を探す
    # 隣接する床マスを
    #   - Dマスまで
    #   - 1マスずつ
    # 再帰的に探索して、通れたところを set にいれて len をとればいけそう

    humidified = set()
    for i in range(h):
        for j in range(w):
            if grid_lines[i][j] == "H":
                humidified = humidified | find_nearby_floor(h, w, i, j, d, grid_lines)

    return len(humidified)


def find_nearby_floor(h, w, i, j, d, grid_lines):
    humidified = set()
    humidified.add((i, j))  # 直下

    # 右
    yoko = j + 1
    if 0 <= yoko <= w - 1:  # 存在するか
        if grid_lines[i][yoko] == ".":
            humidified = humidified | find_nearby_floor(
                h, w, i, yoko, d - 1, grid_lines
            )

    # 左
    yoko = j - 1
    if 0 <= yoko <= w - 1:  # 存在するか
        if grid_lines[i][yoko] == ".":
            humidified = humidified | find_nearby_floor(
                h, w, i, yoko, d - 1, grid_lines
            )

    # 上方向
    tate = i - 1
    if 0 <= tate <= h - 1:
        if grid_lines[tate][j] == ".":  # 存在するか
            humidified = humidified | find_nearby_floor(
                h, w, tate, j, d - 1, grid_lines
            )
    # 下方向
    tate = i + 1
    if 0 <= tate <= h - 1:
        if grid_lines[tate][j] == ".":  # 存在するか
            humidified = humidified | find_nearby_floor(
                h, w, tate, j, d - 1, grid_lines
            )

    return humidified


if __name__ == "__main__":
    h, w, d = map(int, input().split())
    grid_lines = [input() for _ in range(h)]

    print(main(h, w, d, grid_lines))
