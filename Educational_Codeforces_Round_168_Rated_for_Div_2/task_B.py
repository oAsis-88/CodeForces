t = int(input())

for i in range(t):
    n = int(input())
    x = [list(input())]
    x.append(list(input()))

    y = []
    for i in range(2):
        tmp = []
        for j in range(1, n - 1):
            count = 0
            if x[i - 1][j] == '.':
                count += 1
            if x[i][j - 1] == '.':
                count += 1
            if x[i][j + 1] == '.':
                count += 1
            tmp.append(count)
        y.append(tmp)

    res = 0
    for i in range(2):
        for j in range(len(y[0])):
            if y[i][j] == 1 and y[i - 1][j] == 3:
                res += 1
    print(res)
