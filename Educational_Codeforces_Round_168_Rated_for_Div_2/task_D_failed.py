t = int(input())
# t = 1

MAX_A = 1000000000  # 10 ** 9


def df(maps: dict, curr: tuple, lvl: int, max_lvl):
    min_child = MAX_A
    if curr not in maps:
        return curr[1]

    if lvl == max_lvl:
        return curr[1]

    for child in maps[curr]:
        min_child = df(maps, child, lvl + 1, max_lvl)

        if lvl == 0:
            return curr[1] + min_child

        if min_child <= curr[1]:
            return min_child

    return curr[1] + (min_child - curr[1]) // 2


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


    print(df(mapping, (0, a[0]), 0, max(p)))

"""
# n = 4
# a = [0, 1, 0, 2]
# p = [1, 1, 3]

# n = 2
# a = [3, 0]
# p = [1]

# n = 5
# a = [2, 5, 3, 9, 6]
# p = [3, 1, 5, 2]
"""