import math

t = int(input())


def sum_geometric_arithmetic(a, b):
    def sum_i_3i(a, b):
        term1 = 3 * (3 ** a - 3 ** b) / (2 * (1 - 3))
        term2 = 3 ** b * (b - a) / 2
        return term1 - term2

    sum_geom = (3 ** a * (3 ** (b - a) - 1)) / 2
    sum_arith_geom = sum_i_3i(a, b)

    total_sum = 2 * (sum_geom + sum_arith_geom)
    return total_sum


def sum_geometric_progression(a, b):
    # Встроенная функция для вычисления суммы по формуле
    def sum_x(i):
        return 2 * (3 ** i) * (i + 1)

    # Суммируем значения от a до b-1
    total_sum = sum(sum_x(i) for i in range(a, b))
    return total_sum


for _ in range(t):
    l, r = map(int, input().split())

    log_l = int(math.log(l, 3))
    prev_count = (log_l + 1) * 2
    l += 1

    count_l = (log_l + 1) * (3 ** (log_l + 1) - l)
    # print(f"({log_l} + 1) * (3 ** ({log_l} + 1) - {l}) = {count_l}")

    log_r = int(math.log(r, 3))
    count_r = 0
    count = 0
    if log_l < log_r:
        count_r = (log_r + 1) * (r - 3 ** log_r + 1)
        count = sum_geometric_progression(log_l + 1, log_r)
    else:
        prev_count -= 2
    print(f"log_l = {log_l};  log_r = {log_r}")

    print(f"{prev_count} + {count_l} + {count} + {count_r} = {prev_count + count_l + count + count_r}")

"""
1 -> 1
1 2 -> 3 0 -> 1 0 -> 0 0 #  3
1 2 3 -> 3 0 3 -> 1 0 3 -> 1 0 1 -> 0 0 1 -> 0 0 0  # 6
1 2 3 4 -> 3 0 3 4 -> 1 0 3 4 -> 0 0 3 4 -> 0 0 1 4 -> 0 0 0 4 -> 0 0 0 1 -> 0 0 0 0 # 8
1 2 3 4 5 -> 3 0 3 4 5 -> 1 0 3 4 5 -> 0 0 3 4 5 -> 0 0 1 4 5 -> 0 0 0 4 5 -> 0 0 0 1 5 -> 0 0 0 0 5 ->  # 10

2 3 4 -> 0 9 4 -> 0 3 4 -> 0 1 4 -> 0 0 4 -> 0 0 1 -> 0 0 0

4 5 6 7 -> 1 15 6 7 -> 0 15 18 7 -> 0 5 18 7 -> 0 1 18 7 -> 0 0 18 7 -> 0 0 6 7 -> 0 0 2 7 -> 0 0 0 7 -> 0 0 0 2 -> 0 0 0 0  # 12
           1 15 6 7 -> 0 45 6 7  -> 0 15 6 7 -> 0 5 6 7  -> 0 1 6 7  -> 0 0 6 7
1 5 6 7 (2) 0 5 6 7 (4) 0 1 2 2 (7) 



199999 200000 66666 600000 22222


 
"""
