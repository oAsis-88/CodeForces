t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    L, R = map(int, input().split())

    res = 2
    if l <= L <= r <= R:
        res += r - L
    elif l <= L <= R <= r:
        res += R - L
    elif L <= l <= r <= R:
        res += r - l
    elif L <= l <= R <= r:
        res += R - l

    if R < l or r < L:
        res -= 1
    if l == L:
        res -= 1
    if r == R:
        res -= 1

    print(res)

    # [[1, 2], [3, 4]]  # 1
    # [[[1, 2, 3, 4, 5]]]  # 3
    # [1, 2, [3, 4, 5, [6, 7]]]  # 2
    # [1, 2, 3, [4, 5], 6, 7]  # 3
