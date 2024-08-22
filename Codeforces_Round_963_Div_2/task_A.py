t = int(input())


for i in range(t):
    n = int(input())
    s = tuple(input())

    res = min(n, s.count('A')) + min(n, s.count('B')) + min(n, s.count('C')) + min(n, s.count('D'))

    print(res)
