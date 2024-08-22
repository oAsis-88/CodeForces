t = 1

for _ in range(t):
    n, k = map(int, input().split())

    rectangles = []
    maximum = 0
    for _ in range(n):
        a, b = map(int, input().split())
        rectangles.append((min(a, b), max(a, b)))
        maximum += a + b

    if k > maximum:
        print(-1)
        break

    # (3, 4), (2, 9), (8, 10)
    print(rectangles)
    rectangles.sort(key=lambda x: sum(x))
    print(rectangles)
    scores = [0]
    for i in range(len(rectangles)):
        a, b = rectangles[i]
        if len(scores) - 1 + a + b < k:
            scores.append(scores[-1] + a)
        else:
            sum_j = 0
            for j in range(i):

