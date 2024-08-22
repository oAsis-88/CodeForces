t = int(input())

MAX_A = 1000000000001  # 10 ** 9 + 1


def dfs(maps, curr, count):
    if curr not in maps:
        return count <= curr[1]

    if curr[1] < count and curr[0] != 0:
        count += count - curr[1]

    b = True
    for child in maps[curr]:
        b &= dfs(maps, child, count)

    return b


for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))

    mapping = {}
    for i in range(n - 1):
        if (p[i] - 1, a[p[i] - 1]) not in mapping:
            mapping[(p[i] - 1, a[p[i] - 1])] = [(i + 1, a[i + 1])]
        else:
            mapping[(p[i] - 1, a[p[i] - 1])].append((i + 1, a[i + 1]))

    l, r = 0, MAX_A

    while l < r:
        m = (l + r + 1) // 2
        if dfs(mapping, (0, a[0]), m):
            l = m
        else:
            r = m - 1

    print(l + a[0])
