def main(k, values):
    return [value // k for value in values if value % k == 0]


if __name__ == "__main__":

    _, k = map(int, input().split())

    values = [int(i) for i in (input().split())]

    print(" ".join(map(str, main(k, values))))
