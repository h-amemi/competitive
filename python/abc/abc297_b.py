s = input()


def main():
    # S において左から x,y (x<y) 文字目が B であるとする。このとき x と y の偶奇が異なる。
    b_sum = 0  # 偶奇がことなるということは、それぞれを合算したら奇数
    r_indexes = []
    k_index = -1
    for i, chara in enumerate(s):
        if chara == "B":
            b_sum += i
        if chara == "R":
            r_indexes.append(i)
        if chara == "K":
            k_index = i
    if b_sum % 2 == 0:
        print("No")
        return

    # K は 2 つの R の間にある。より形式的には、S において左から x,y (x<y) 文字目が R であり、 z 文字目が K であるとする。このとき、 x<z<y が成り立つ。
    if not r_indexes[0] < k_index < r_indexes[1]:
        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
