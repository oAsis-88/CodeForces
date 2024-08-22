t = int(input())

for _ in range(t):
    n = int(input())
    s = list(sorted(map(int, input().split())))

    odd_index = len(s) - 1
    while odd_index >= 0 and s[odd_index] % 2 == 0:
        odd_index -= 1

    if s[odd_index] % 2 == 0:
        print(0)
        continue

    max_odd = s[odd_index]
    count = 0
    count_after = 0

    for i in range(len(s)):
        if s[i] % 2 == 0:
            if s[i] < max_odd:
                count += 1
                max_odd += s[i]
            else:
                count_after += 1

    if count_after > 0:
        count += count_after + 1

    print(count)

# 2 4 6 8 9999 990_000 1_000_000

# 10019 990_000 1_000_000

# 1_010_019