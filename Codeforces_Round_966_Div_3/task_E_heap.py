from heapq import heappop, heappush, heapify

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    w = int(input())

    a = list(sorted(map(int, input().split())))

    res = 0
    heap = []

    arr_sum = [1]
    for i in range(1, (m + 1) // 2):
        if m - k < i:
            arr_sum.append(arr_sum[-1])
        else:
            arr_sum.append(min(arr_sum[-1] + 1, k))

    arr_sum.extend(arr_sum[m // 2 - 1::-1])
    matrix = [[0 for i in range(m)] for j in range(n)]
    matrix[0] = arr_sum

    for el in arr_sum:
        heappush(heap, -1 * el)

    for i in range(1, (n + 1) // 2):
        for j in range(m):
            # сложение с предыдущей строкой, общий максимум, максимум на данной строке, не превышает половину
            matrix[i][j] = min((i + 1) * arr_sum[j], k * k, (j + 1) * k)
            heappush(heap, -1 * min((i + 1) * arr_sum[j], k * k, (j + 1) * k))

    for i in range((n + 1) // 2, n):
        matrix[i] = matrix[min(n - i - 1, n - k)]
        for el in matrix[i]:
            heappush(heap, -1 * el)

    while a:
        res += -1 * heappop(heap) * a.pop()

    print(res)

    # res = 0
    # i = 0
    # while a and i < w:
    #
    #     count = (n - k + i + 1) * (m - k + i + 1) - (n - k + i) * (m - k + i)
    #     if k == 0:
    #         count -= 4
    #
    #     while a and count > 0:
    #         tmp = a.pop(0) * min((k - i + 1) * (k - i + 1), k * k)
    #         res += tmp
    #         count -= 1
    #     i += 1
    #     k -= 1
    #
    # print(res)
