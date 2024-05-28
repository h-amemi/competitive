def main(n, grid_a, grid_b):
    for i in range(n):
        for j in range(n):
            if grid_a[i][j] != grid_b[i][j]:
                return i + 1, j + 1
    pass


if __name__ == "__main__":
    n = int(input())

    grid_a = [[i for i in input()] for _ in range(n)]
    grid_b = [[i for i in input()] for _ in range(n)]

    i, j = main(n, grid_a, grid_b)

    print(f"{i} {j}")
