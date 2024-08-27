def main(sakebu, neru, okiru):
    # 起きる時間をベースに 24 時間表記を調整
    sakebu += 24 if sakebu < okiru else 0
    neru += 24 if neru < okiru else 0

    return okiru <= sakebu <= neru


if __name__ == "__main__":
    sakebu, neru, okiru = map(int, input().split())
    print("Yes" if main(sakebu, neru, okiru) else "No")
