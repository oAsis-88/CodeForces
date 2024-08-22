t = int(input())

N = 2 * 10 ** 5

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    low = a[0]
    hight = a[0]

    for i in range(1, len(a)):
        if a[i] < low - 1 or a[i] > hight + 1:
            print("NO")
            break

        hight = max(hight, a[i])
        low = min(low, a[i])
    else:
        print("YES")