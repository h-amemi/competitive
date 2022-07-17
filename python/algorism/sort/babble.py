import argparse


def sort(l):
    sorted = []
    while 0 < len(l):
        minimum = None
        minimum_index = None
        for i, n in enumerate(l):
            if minimum is None or n < minimum:
                minimum = n
                minimum_index = i
        sorted.append(minimum)
        del l[minimum_index]
    return sorted


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--integers", metavar="N", type=int, nargs="+", help="Integers for sort"
    )
    args = parser.parse_args()
    print(sort(args.integers))
