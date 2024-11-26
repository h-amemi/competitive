def main(toys, boxes):
    toys_desc = sorted(toys, reverse=True)
    boxes_desc = sorted(boxes, reverse=True)

    buy_box = None
    for i in range(len(toys_desc)):
        if toys_desc[i] <= boxes_desc[i]:
            continue
        if buy_box is None:
            buy_box = toys_desc[i]
            boxes_desc.insert(i, buy_box)
        else:
            return -1
    return buy_box


if __name__ == "__main__":
    n = int(input())
    toys = [int(i) for i in (input().split())]
    boxes = [int(i) for i in (input().split())]

    print(main(toys, boxes))
