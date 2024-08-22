t = int(input())

# t = 1
max_score = 10000000

for _ in range(t):
    n, k = map(int, input().split())
    # n, k = 3, 25
    # rectangles = [(2, 9), (3, 4), (8, 10)]
    # maximum = sum(sum(el) for el in rectangles)

    rectangles = []
    maximum = 0

    for _ in range(n):
        a, b = map(int, input().split())
        rectangles.append((min(a, b), max(a, b)))
        maximum += a + b

    if k > maximum:
        print(-1)
        continue

    rectangles.sort(key=lambda x: sum(x))
    # print(rectangles)
    scores = [0] + [max_score] * maximum
    # scores = [max_score]
    # print(scores)
    for i in range(len(rectangles)):
        a, b = rectangles[i]

        curr_sum = 1
        # print('-----', a, '-----')
            # print('    -----', scores[curr_sum], '-----')
                    # scores[z + 1 + j * curr_sum] = min(scores[z + j * curr_sum], scores[j * curr_sum - 1] + l)
                    # print('          -----', scores[z + j * curr_sum], scores[j * curr_sum] + l, '-----')
        for j in range(i + 1):
            # print('    -----', a, '+ [', curr_sum, ']-----')
            # print('    -----', a + scores[curr_sum - 1], scores[curr_sum], '-----')
            # if a + scores[curr_sum - 1] < scores[curr_sum]:
            l, r = a, b
            curr_score_rect = 0
            for z in range(1, a + b + 1):
                curr_score_rect += l
                # print('          -----', scores[z + curr_sum - 1], scores[curr_sum - 1] + curr_score_rect, end=" = ")
                scores[z + curr_sum - 1] = min(scores[z + curr_sum - 1], scores[curr_sum - 1] + curr_score_rect)
                # print(scores[z + curr_sum - 1], '-----')
                r -= 1
                l, r = min(l, r), max(l, r)
            curr_sum += sum(rectangles[j])
        # print(scores)

    # print(k)
    print(scores)
    print(maximum)
    print(len(scores))
    print(scores[k])



"""
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1 -> 

3 25
9 2
4 3
8 10

7

1 4
6 3

1 5
4 4

5 10
1 1
1 1
1 1
1 1
1 1

2 100
1 2
5 6

3 11
2 2
3 3
4 4

3 25
9 2
4 3
8 10

4 18
5 4
8 5
8 3
6 2

"""
