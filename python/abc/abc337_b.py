def is_abc_string(s):
    chars = ["A", "B", "C"]

    index = 0
    for char in chars:
        while index < len(s) and s[index] == char:
            index += 1

    return len(s) == index


if __name__ == "__main__":
    s = input()

    print("Yes" if is_abc_string(s) else "No")
