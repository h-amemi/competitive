from collections import defaultdict


def main():
    _ = input()
    s = input()

    max_length_by_char = defaultdict(int)

    current_char = s[0]
    current_length = 1
    for char_ in s[1:]:
        if char_ == current_char:
            current_length += 1
        else:
            if current_length >= max_length_by_char[current_char]:
                max_length_by_char[current_char] = current_length

            current_char = char_
            current_length = 1
    else:
        if current_length >= max_length_by_char[current_char]:
            max_length_by_char[current_char] = current_length

    combinations = 0
    for v in max_length_by_char.values():
        combinations += v

    print(combinations)


if __name__ == "__main__":
    main()
