"""
ABC086C - Traveling

t2 - t1 の時間で t2 の場所に移動できるのかの探索の連続
その探索については全探索で一旦やってみる
探索だるいな・・・
- `t - latest_t == abs(x - latest_x) + abs(y - latest_y)` なら大丈夫
- 行って戻ったケースを考慮する
    ```
    a = (t - latest_t) - abs(x - latest_x) + abs(y - latest_y)
    return (0 <= a and a % 2 == 0)
    ```
"""

N = int(input())
t_s = [tuple([int(s) for s in input().split()]) for _ in range(N)]


def is_idou_possible():
    latest_t = 0
    latest_x = 0
    latest_y = 0

    for t, x, y in t_s:
        abs_distance = abs(x - latest_x) + abs(y - latest_y)
        jikan = t - latest_t
        jikan_amari = jikan - abs_distance
        if not (0 <= jikan_amari and jikan_amari % 2 == 0):
            return False

        latest_t = t
        latest_x = x
        latest_y = y

    return True


print("Yes" if is_idou_possible() else "No")
