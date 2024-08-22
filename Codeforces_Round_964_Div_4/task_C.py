t = int(input())

for _ in range(t):
    n, s, m = map(int, input().split())

    start = 0
    boolean = False
    for i in range(n):
        l, r = map(int, input().split())
        if l - start >= s:
            boolean = True
        start = r

    if m - start >= s:
        boolean = True

    if boolean:
        print('YES')
    else:
        print('NO')
