import heapq

n = 5
m = 5
k = 2

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
    heapq.heappush(heap, el)

for i in range(1, (n + 1) // 2):
    for j in range(m):
        print(i * min(k, n - k), j * min(k, m - k))
        # сложение с предыдущей строкой, общий максимум, максимум на данной строке, не превышает половину
        matrix[i][j] = min((i + 1) * arr_sum[j],
                           k * k,
                           k * (j + 1), k * (m - j),
                           (m - k + 1) * (j + 1), (m - k + 1) * (m - j),
                           (n - k + 1) * (m - k + 1),
                           (n - k + 1) * (j + 1), (n - k + 1) * (m - j))
        heapq.heappush(heap, min((i + 1) * arr_sum[j], k * k, (j + 1) * k))

for i in range((n + 1) // 2, n):
    matrix[i] = matrix[min(n - i - 1, n - k)]
    for el in matrix[i]:
        heapq.heappush(heap, el)

print(f"1: {heap.count(1)}")
print(f"2: {heap.count(2)}")
print(f"3: {heap.count(3)}")
print(f"4: {heap.count(4)}")
print(f"6: {heap.count(6)}")
print(f"8: {heap.count(8)}")
print(f"9: {heap.count(9)}")
print(f"10: {heap.count(10)}")
print(f"12: {heap.count(12)}")
print(f"16: {heap.count(16)}")

for mat in matrix:
    print(mat)
