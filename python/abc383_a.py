def main(n, t_v_list):
    water_ = 0
    time_ = 0

    for t, v in t_v_list:
        time_diff = t - time_
        water_ -= time_diff  # 時間経過による水の減少
        if water_ < 0:
            water_ = 0
        water_ += v
        time_ = t
    return water_


if __name__ == "__main__":
    n = int(input())
    t_v_list = [(int(a), int(b)) for a, b in (input().split() for _ in range(n))]

    print(main(n, t_v_list))
