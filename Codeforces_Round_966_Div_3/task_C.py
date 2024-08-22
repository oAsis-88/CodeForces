t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())

    for _ in range(m):
        s = input()
        if len(s) != len(a):
            print("NO")
            continue

        dict_char_int = {s[0]: a[0]}
        dict_int_char = {a[0]: s[0]}
        i = 1
        while i < len(a):
            if s[i] not in dict_char_int and a[i] not in dict_int_char:
                dict_char_int[s[i]] = a[i]
                dict_int_char[a[i]] = s[i]
            elif ((s[i] in dict_char_int and dict_char_int[s[i]] != a[i]) or
                  (a[i] in dict_int_char and dict_int_char[a[i]] != s[i])):
                print("NO")
                break
            i += 1
        else:
            print("YES")
