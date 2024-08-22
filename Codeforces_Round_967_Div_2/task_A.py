import collections

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    num_count = collections.Counter(a)
    print(len(a) - max(num_count.values()))
