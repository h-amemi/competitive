def main(a, b, ds):
    # どこかの間が b (平日分) 日あいていれば、全部休日に入っている

    week = a + b

    # 曜日の重複を削除する
    ds = sorted(list(set([d % week for d in ds])))
    ds.append(ds[0] + week)  # 最後の日 + 0 個めの予定の間も考慮

    return any(ds[i + 1] - ds[i] > b for i in range(len(ds) - 1))


def main_ososugita(a, b, ds):
    # 基点を1日ずつずらしてすべてが休日か確認する

    week = a + b

    # 曜日の重複を削除する
    ds = sorted(list(set([d % week for d in ds])))

    for i in range(week):
        yasumi = a + i
        if all(i < d < yasumi for d in ds):
            return True
    False


if __name__ == "__main__":
    _, a, b = map(int, input().split())

    ds = [int(i) for i in (input().split())]

    print("Yes" if main(a, b, ds) else "No")
