import argparse


def sort(l):
    """
    pivot を真ん中にして、左右で入れ替え対象を見つけて入れ替える、というのを愚直にやってみる
    """

    if len(l) <= 1:
        return l

    pivot = len(l) // 2
    pivot_val = l[pivot]

    hidari_idx = 0
    migi_idx = len(l)

    while True:
        # 1ループ1つ入れ替える
        # pivot に対しての処理がおわるまで
        irekae_hidari_dekai = None
        irekae_hidari_dekai_val = None
        irekae_migi_chiisai = None
        irekae_migi_chiisai_val = None
        # pivot より小さいやつ見つける
        for i in range(hidari_idx, pivot + 1):  # pivot まで含むようにする
            val = l[i]
            if val >= pivot_val:
                # 入れ替え対象
                irekae_hidari_dekai = i
                irekae_hidari_dekai_val = val
                break

        # pivot より大きいやつみつける
        for i in reversed(range(pivot, migi_idx)):
            val = l[i]
            if val <= pivot_val:
                # 入れ替え対象
                irekae_migi_chiisai = i
                irekae_migi_chiisai_val = val
                break

        if irekae_hidari_dekai_val == irekae_migi_chiisai_val:
            break

        l[irekae_hidari_dekai] = irekae_migi_chiisai_val
        l[irekae_migi_chiisai] = irekae_hidari_dekai_val

        hidari_idx = irekae_hidari_dekai
        migi_idx = irekae_migi_chiisai + 1

        # pivot が変わる場合の対応
        if pivot == irekae_hidari_dekai:
            pivot = irekae_migi_chiisai
            continue

        if pivot == irekae_migi_chiisai:
            pivot = irekae_hidari_dekai
            continue

    le = l[0:pivot]
    mi = l[pivot : pivot + 1]
    ri = l[pivot + 1 :]

    return sort(le) + mi + sort(ri)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--integers", metavar="N", type=int, nargs="+", help="Integers for sort"
    )
    args = parser.parse_args()
    print(sort(args.integers))
