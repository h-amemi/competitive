def main(n, m, umare_list):
    # 長男が既にいるかを管理するリストを作る
    chonan_list = [0] * n

    for umare in umare_list:
        ie = int(umare[0]) - 1
        if umare[1] == "M" and chonan_list[ie] == 0:
            print("Yes")
            chonan_list[ie] += 1
        else:
            print("No")


if __name__ == "__main__":
    n, m = map(int, input().split())

    umare_list = [input().split() for _ in range(m)]

    main(n, m, umare_list)
