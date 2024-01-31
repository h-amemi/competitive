def main(scores):
    sum = 0
    for score_a, score_b in scores:
        sum += score_a - score_b

    return "Draw" if sum == 0 else "Takahashi" if sum > 0 else "Aoki"


if __name__ == "__main__":
    n = int(input())
    scores = [tuple(int(i) for i in input().split()) for _ in range(n)]

    print(main(scores))
