t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    n, m = min(n, m), max(n, m)
    w = int(input())

    a = list(sorted(map(int, input().split())))

    res = 0

    arr_sum = []

    for i in range(n):
        for j in range(m):
            arr_sum.append(min(i + 1, k, n - i, n - k + 1) * min(j + 1, k, m - j, m - k + 1))

    from collections import Counter
    print(Counter(arr_sum))

    for index in range(0, len(arr_sum), m):
        print(arr_sum[index: index + m])

    arr_sum.sort()
    while a:
        res += arr_sum.pop() * a.pop()

    print(res)

"""
1
7 8 2
9
1 1 1 1 1 1 1 1 1
"""