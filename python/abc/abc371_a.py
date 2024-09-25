def main(ab, ac, bc):
    # それぞれに対して、大なりであったほうをカウント
    # カウントが1である人が2番目に年上
    a_count = 0
    b_count = 0
    c_count = 0

    if ab == ">":
        a_count += 1
    else:
        b_count += 1

    if ac == ">":
        a_count += 1
    else:
        c_count += 1

    if bc == ">":
        b_count += 1
    else:
        c_count += 1

    if a_count == 1:
        return "A"
    elif b_count == 1:
        return "B"
    else:
        return "C"


if __name__ == "__main__":
    ab, ac, bc = tuple(input().split())

    print(main(ab, ac, bc))
