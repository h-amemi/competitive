def sanitize(n, m, values):
    hands = 0
    for i, value in enumerate(values):
        hands += value
        if hands == m:
            return i + 1
        elif hands > m:
            return i

    return n


if __name__ == "__main__":
    n, m = map(int, input().split())
    values = [int(i) for i in (input().split())]

    print(sanitize(n, m, values))
