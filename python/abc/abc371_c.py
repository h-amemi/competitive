import itertools


def main():
    # "同型"がむずかしい
    # - G, H の各頂点の対応の組み合わせ
    # - それぞれの辺が違ったら操作を行うを繰り返す
    # でできそう

    edges_g = set()
    edges_h = set()
    n = int(input())
    m_g = int(input())
    for i in range(m_g):
        a, b = map(int, input().split())
        edges_g.add(tuple(a - 1, b - 1))
        edges_g.add(tuple(b - 1, a - 1))

    m_h = int(input())
    for i in range(m_h):
        a, b = map(int, input().split())
        edges_h.add(tuple(a - 1, b - 1))
        edges_h.add(tuple(b - 1, a - 1))

    costs = [[int(i) for i in (input().split())] for _ in range(n)]

    # 選択肢の全組み合わせに対して
    for i in itertools.product(list(range(n))):
        print(i)

    pass


if __name__ == "__main__":

    # int list
    values = [int(i) for i in (input().split())]

    # int a, b, c
    a, b, c = map(int, input().split())

    # int list (n lines)
    values = [[int(i) for i in (input().split())] for _ in range(n)]

    print(main())
