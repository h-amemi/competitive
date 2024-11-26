def main(s):
    counts = []
    count = 0
    s = s[1:]  # 最初の | は抜く
    for char_ in s:
        if char_ == "-":
            count += 1
            continue
        counts.append(count)
        count = 0

    return counts


if __name__ == "__main__":
    s = input()

    print(" ".join(map(str, main(s))))
