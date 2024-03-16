def main(s):
    start = s[0:1]
    end = s[-1]
    mid = s[1:-1]

    return True if start == "<" and end == ">" and mid == "=" * len(mid) else False


if __name__ == "__main__":
    s = input()

    print("Yes" if main(s) else "No")
