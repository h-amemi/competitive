import math


def main(n, s_cost, s_mount, m_cost, m_mount, l_cost, l_mount):
    """
    一番コスパいいもので大半を買って、それ以降は組み合わせで探索する
    """
    price_by_1_s = s / s_mount
    price_by_1_m = m / m_mount
    price_by_1_l = l / l_mount

    # 一番コスパいいもので買い続けた余りをだす
    if price_by_1_s < price_by_1_m < price_by_1_l:
        amari, buy_cost = calc_amari_mount_with_cost(n, l_mount, s_mount, s_cost)
    elif price_by_1_m < price_by_1_l:
        amari, buy_cost = calc_amari_mount_with_cost(n, l_mount, m_mount, m_cost)
    else:
        amari, buy_cost = calc_amari_mount_with_cost(n, l_mount, l_mount, l_cost)

    # amari, buy_cost = n, 0

    # あまりについて、全探索で一番安いパターンを探す
    # いったん l で全部買った時のコストを初期値にする
    yasui_cost = l_cost * (math.ceil(amari / l_mount))

    for l_kau in range(math.ceil(amari / l_mount) + 1):
        l_katta_amari = max(amari - (l_kau * l_mount), 0)  # マイナスにならないように
        for m_kau in range(math.ceil(l_katta_amari / m_mount) + 1):
            m_katta_amari = max(l_katta_amari - (m_kau * m_mount), 0)

            s_kau = math.ceil(m_katta_amari / s_mount)

            yasui_cost = min(
                yasui_cost, (l_kau * l_cost + m_kau * m_cost + s_kau * s_cost)
            )

    return buy_cost + yasui_cost


def calc_amari_mount_with_cost(n, l_mount, mount, cost):
    # n が l_mount 個以下の場合、n - l_mount がマイナスになるので、確定するのは 0 個
    buy_pack = max((n - (8 * 12)) // mount, 0)
    amari = n - (mount * buy_pack)
    buy_cost = cost * buy_pack

    return amari, buy_cost


if __name__ == "__main__":
    n, s, m, l = tuple([int(i) for i in (input().split())])

    print(main(n, s, 6, m, 8, l, 12))
