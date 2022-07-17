"""
ABC049C - 白昼夢

- dream dreamer erase eraser
- suffix の "er" と　"erase" の "er" がかぶってるのがミソ
- ケツからやってけばいける気がする

>>> print("dream"[::-1])
maerd
>>> print("dreamer"[::-1])
remaerd
>>> print("erase"[::-1])
esare
>>> print("eraser"[::-1])
resare
"""

S = input()


def is_t(s):
    reversed_s = s[::-1]

    reversed_dream = "maerd"
    reversed_dreamer = "remaerd"
    reversed_erase = "esare"
    reversed_eraser = "resare"

    while 0 < len(reversed_s):
        if reversed_s.startswith(reversed_dream):
            reversed_s = reversed_s[5:]
            continue

        if reversed_s.startswith(reversed_dreamer):
            reversed_s = reversed_s[7:]
            continue

        if reversed_s.startswith(reversed_erase):
            reversed_s = reversed_s[5:]
            continue

        if reversed_s.startswith(reversed_eraser):
            reversed_s = reversed_s[6:]
            continue

        return False

    return True


print("YES" if is_t(S) else "NO")
