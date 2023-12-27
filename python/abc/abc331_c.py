def main(values):
    # 順番に見るだけだと計算量が多すぎて制限時間 over
    sums = [
        str(sum([v for v in (values[:i] + values[i + 1 :]) if value < v]))
        for i, value in enumerate(values)
    ]

    # コンテストの解説ページを参考
    # https://atcoder.jp/contests/abc331/editorial/7806

    values_with_index = [(i, value) for i, value in enumerate(values)]
    sorted_values = sorted(values_with_index, key=lambda x: x[1])

    sums = [0] * len(values) + 1
    for i, value in sorted_values:
        sum_ = 0
        for _, value_ in sorted_values[:0]:
            sum_ += value_
        sums[i] = sum_

    return sums


if __name__ == "__main__":
    _ = input()
    values = [int(i) for i in (input().split())]

    sums = main(values)
    print(" ".join(sums))
