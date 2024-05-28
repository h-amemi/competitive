def main(n, values):
    stack = []
    for value in values:
        stack.append(value)

        while len(stack) != 1 and stack[-2] == stack[-1]:
            if stack[-2] == stack[-1]:
                stack[-2] += 1
                del stack[-1]

    return len(stack)


if __name__ == "__main__":
    n = int(input())

    values = [int(i) for i in (input().split())]

    print(main(n, values))
