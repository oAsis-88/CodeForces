def get_minimums(*arrays):
    # Находим длину самого длинного массива
    max_length = max(len(arr) for arr in arrays)

    # Создаем новый массив, где будет сохраняться минимальные значения
    min_array = []

    # Проходимся по каждому индексу
    for i in range(max_length):
        # Собираем элементы из всех массивов для текущего индекс
        values_at_index = [arr[i] for arr in arrays if i < len(arr)]
        min_array.append(min(values_at_index))

    return min_array

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
b = [7, 14, 20, 26, 31, 36, 40, 44, 47, 50, 52, 54, 55, 56, 56]
c = [3, 6, 9, 11, 13, 14, 15, 15]
d = [9, 18, 26, 34, 41, 48, 54, 60, 65, 70, 74, 78, 81, 84, 86, 88, 89, 90, 90]

b2 = [el + a[-1] for el in b]
c2 = [el + a[-1] for el in c]
d2 = [el + a[-1] for el in d]
# print(b2)
print(c2)
# print(d2)

b3 = [el + c2[-1] for el in b2]
d3 = [el + c2[-1] for el in d2]

print(b3)
# print(d3)

d4 = [el + b3[-1] for el in d3]

print(d4)
