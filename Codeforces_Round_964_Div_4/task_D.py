T = int(input())

for _ in range(T):
    s = list(input())
    t = input()

    i = 0
    index = 0
    while i < len(s) and index < len(t):
        if s[i] == t[index] or s[i] == "?":
            if s[i] == "?":
                s[i] = t[index]
            if index < len(t):
                index += 1
        i += 1

    while i < len(s):
        if s[i] == "?":
            s[i] = t[index - 1]
        i += 1

    if index == len(t):
        print("YES")
        print("".join(s))
    else:
        print("NO")
