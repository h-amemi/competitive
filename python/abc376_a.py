def main(c, values):
    last = values[0]
    counter = 1
    for value in values[1:]:
        if value - last >= c:
            counter += 1
            last = value
    return counter


if __name__ == "__main__":
    _, c = map(int, input().split())

    values = [int(i) for i in (input().split())]

    print(main(c, values))
