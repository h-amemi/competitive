def get_minimum_divisor(n, divisors, i):
    for j in divisors:
        if i % (n / j) == 0:
            return j
    return None


def main():
    n = int(input())

    # 1 ～ 9 のうち N の約数
    divisors = [i for i in range(1, 10) if n % i == 0]

    result = ""
    for i in range(n + 1):
        minimum_divisor = get_minimum_divisor(n, divisors, i)
        result += str(minimum_divisor) if minimum_divisor is not None else "-"
    print(result)


if __name__ == "__main__":
    main()
