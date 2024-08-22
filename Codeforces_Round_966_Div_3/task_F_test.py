# rectangle_size = 2x9
from collections import defaultdict

rectangles = [(2, 9), (3, 4), (8, 10)]
k = 25

maximum = sum(sum(pair) for pair in rectangles)
print(maximum)

if k > maximum:
    print(-1)
    exit()

scores = [0]
a = 1
b = 9

for j in range(1, a + b + 1):
    scores.append(scores[-1] + a)
    b -= 1
    a, b = min(a, b), max(a, b)

print(scores)

scores = [0]
a = 7
b = 8

for j in range(1, a + b + 1):
    scores.append(scores[-1] + a)
    b -= 1
    a, b = min(a, b), max(a, b)

print(scores)

scores = [0]
a = 3
b = 5

for j in range(1, a + b + 1):
    scores.append(scores[-1] + a)
    b -= 1
    a, b = min(a, b), max(a, b)

print(scores)

scores = [0]
a = 9
b = 10

for j in range(1, a + b + 1):
    scores.append(scores[-1] + a)
    b -= 1
    a, b = min(a, b), max(a, b)

print(scores)
print()

scores = [0]
a = 3
b = 4

for j in range(1, a + b + 1):
    scores.append(scores[-1] + a)
    b -= 1
    a, b = min(a, b), max(a, b)

print(scores)

# (2, 9), (3, 4), (8, 10)
for i in range(len(rectangles) - 2, -1, -1):
    a, b = rectangles[i]
    length_rect = []
    for j in range(1, a + b + 1):
        scores[j] = min(scores[j], scores[j - 1] + a)
        scores.append(scores[-1] + a)

print(scores)
print(scores[k])

"""
3 4 -> (12, 7)
4 3 -> (12, 7)
4 4 -> (16, 8)
"""