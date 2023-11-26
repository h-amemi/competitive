def main():
    _ = input()
    i_list = [int(i) for i in input().split()]

    sorted_non_duplicate_i_list = sorted(list(set(i_list)))

    print(sorted_non_duplicate_i_list[-2])


if __name__ == "__main__":
    main()
