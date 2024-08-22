t = int(input())

for _ in range(t):
    n = int(input())

    xs = map(int, input().split())

    sxs = set(xs)
    if len(sxs) > 2 or abs(sxs.pop() - sxs.pop()) < 2:
        print("NO")
    else:
        print("YES")
