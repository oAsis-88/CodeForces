t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = list(input())

    l, r = 0, len(a) - 1
    count = 0
    sum_a = sum(a)
    while l < r:
        while l < r and s[l] != 'L':
            sum_a -= a[l]
            l += 1
        while l < r and s[r] != 'R':
            sum_a -= a[r]
            r -= 1
        if l >= r:
            break
        count += sum_a
        sum_a -= (a[l] + a[r])
        l += 1
        r -= 1

    print(count)
