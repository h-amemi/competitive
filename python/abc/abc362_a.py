def main(values, color):
    match color:
        case "Red":
            del values[0]
        case "Green":
            del values[1]
        case "Blue":
            del values[2]
    return min(values)


if __name__ == "__main__":
    values = [int(i) for i in (input().split())]

    color = input()

    print(main(values, color))
