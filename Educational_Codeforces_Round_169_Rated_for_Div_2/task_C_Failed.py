t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    res = 0
    i = 0
    while i < n - 1:
        if k > 0:
            res += a[i + 1] - a[i] - min(k, a[i + 1] - a[i])
            k -= min(k, a[i + 1] - a[i])
        else:
            res += a[i] - a[i + 1]
        i += 2

    if n % 2 != 0:
        res += a[-1]
    print(res)

# 1 2 8 10