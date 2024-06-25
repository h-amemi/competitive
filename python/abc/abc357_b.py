def upper_and_lower(s):
    lower_chars = 0
    for char_ in s:
        lower_chars += 1 if char_.islower() else 0
    return s.upper() if len(s) // 2 >= lower_chars else s.lower()


if __name__ == "__main__":
    s = input()

    print(upper_and_lower(s))
