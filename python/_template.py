def main():
    pass


if __name__ == "__main__":
    # n
    n = int(input())

    # int list
    values = [int(i) for i in (input().split())]

    # int a, b, c
    a, b, c = map(int, input().split())

    # int list (n lines)
    values = [[int(i) for i in (input().split())] for _ in range(n)]

    # list of tuple (str, int)
    values = [(a, int(b)) for a, b in (input().split() for _ in range(n))]

    print(main())
