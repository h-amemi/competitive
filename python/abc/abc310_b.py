N, M = tuple(int(i) for i in input().split())
shouhin_lines = [[int(i) for i in input().split()] for _ in range(N)]
shouhins = [
    {"p": shouhin[0], "c": shouhin[1], "set": set(shouhin[2:])}
    for shouhin in shouhin_lines
]


def is_sperior(i, j):
    return (
        (i["p"] <= j["p"]) # 安いか同じ
        and (i["set"] >= j["set"]) # 少なくとも同じ機能を持っているか
        and (i["p"] < j["p"] or i["c"] > j["c"]) # 安い もしくは 機能が多い
    )


def main():
    for i, shouhin_i in enumerate(shouhins):
        for shouhin_j in shouhins[i + 1 :]:
            if is_sperior(shouhin_i, shouhin_j) or is_sperior(shouhin_j, shouhin_i):
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
