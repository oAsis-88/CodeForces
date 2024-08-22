t = int(input())


def validate(a, b, n):
    for i in range(n - 1):
        if (a[i] & a[i + 1]) != b[i]:
            return False
    return True


for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    b = [0] + b + [0]
    a = [0] * (n + 1)

    for i in range(1, n + 1):
        a[i] = (
                b[i - 1] |
                b[i])

    if validate(a, b, n):
        for el in a[1:]:
            print(el, end=" ")
        print()
    else:
        print(-1)
