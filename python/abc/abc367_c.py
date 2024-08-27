import itertools


def main(n, k, values):
    ret = []

    # 組み合わせの選択肢を作る [[1, 2], [1], [1, 2, 3]]
    choices = [[j + 1 for j in range(values[i])] for i in range(n)]

    # 選択肢の全組み合わせに対して、k で割り切れるか判定
    for i in itertools.product(*choices):
        if sum(i) % k == 0:
            ret.append(i)
    return ret


if __name__ == "__main__":
    n, k = map(int, input().split())
    values = [int(i) for i in (input().split())]

    sum_k_s = main(n, k, values)
    for sum_k in sum_k_s:
        print(" ".join([str(i) for i in sum_k]))
