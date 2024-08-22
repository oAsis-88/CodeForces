t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    res = min(n * m, n * k, m * k, k * k)
    print(res)
