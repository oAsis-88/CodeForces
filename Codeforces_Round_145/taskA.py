t = int(input())

result = ""

for i in range(t):
    element = input()
    el = list(element)
    unique = set(el)
    count = el.count(el[0])
    if len(unique) == 1:
        result += "-1\n"
    elif len(unique) == 2 and count == 1 or count == 3:
        result += "6\n"
    else:
        result += "4\n"

print(result)


