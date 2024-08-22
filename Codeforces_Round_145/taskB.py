t = int(input())
res = ""
for i in range(t):
    element = int(input()) - 1
    if element == 0:
        res += "0\n"
        continue
    res += f"{int(element ** 0.5)}\n"

print(res)