import math


def will_touch_circle(x1, y1, x2, y2, cx, cy, r):
    """Проверяет пересечение линии от (x1, y1) до (x2, y2) с окружностью"""
    dx, dy = x2 - x1, y2 - y1
    fx, fy = x1 - cx, y1 - cy

    a = dx * dx + dy * dy
    b = 2 * (fx * dx + fy * dy)
    c = fx * fx + fy * fy - r * r

    discriminant = b * b - 4 * a * c

    if discriminant >= 0:
        discriminant = math.sqrt(discriminant)
        t1 = (-b - discriminant) / (2 * a)
        t2 = (-b + discriminant) / (2 * a)

        if 0 <= t1 <= 1 or 0 <= t2 <= 1:
            return True
    return False


def can_reach_without_touching(n, circles, start, target):
    sx, sy = start
    tx, ty = target

    for i, (cx, cy) in enumerate(circles):
        r_start = 0  # Радиус в начальный момент времени (0)
        r_end = i + 1  # Радиус через (i + 1) секунд
        if will_touch_circle(sx, sy, tx, ty, cx, cy, r_end):
            return "NO"

    return "YES"


# Пример данных
test_data = [
    (3, [(2, 5), (2, 14), (10, 13)], (4, 9), (9, 7)),
    (3, [(10, 11), (6, 9), (12, 12)], (14, 13), (4, 8)),
    (1, [(5, 7)], (12, 6), (11, 13)),
    (2, [(1000000000, 2), (2, 1000000000)], (1, 1), (2, 2)),
    (1, [(999999998, 1000000000)], (999999999, 999999999), (1, 1)),
    (1, [(1000000000, 1)], (1, 1000000000), (1, 1)),
    (10, [(989237121, 2397081), (206669655, 527238537), (522705783, 380636165),
          (532545346, 320061691), (207818728, 199485303), (884520552, 315781807),
          (992311437, 802563521), (205138355, 324818663), (223575704, 395073023),
          (281560523, 236279118)], (216941610, 572010615), (323956540, 794523071))
]

# Запуск и вывод результатов
for n, circles, start, target in test_data:
    result = can_reach_without_touching(n, circles, start, target)
    print(result)
