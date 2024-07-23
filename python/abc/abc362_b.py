def main(a, b, c):
    # 三平方の定理で頑張る
    # いずれかの辺の長さが a**2 + c**2 = c**2 であれば直角三角形

    # それぞれの辺の長さの2乗
    a_b = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    a_c = (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2
    b_c = (b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2

    return a_b == (a_c + b_c) or a_c == (a_b + b_c) or b_c == (a_b + a_c)


if __name__ == "__main__":
    a = [int(i) for i in (input().split())]
    b = [int(i) for i in (input().split())]
    c = [int(i) for i in (input().split())]

    print("Yes" if main(a, b, c) else "No")
