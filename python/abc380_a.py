def main(n):
    return (
        is_x_in_n_x_times("1", n)
        and is_x_in_n_x_times("2", n)
        and is_x_in_n_x_times("3", n)
    )


def is_x_in_n_x_times(x: str, n: str):
    count = 0
    for n_char in n:
        count += 1 if x == n_char else 0

    return int(x) == count


if __name__ == "__main__":
    n = input()

    print("Yes" if main(n) else "No")
