t = int(input())

for _ in range(t):
    a = input()

    if int(a) > 101 and int(a[:2]) == 10 and a[2] != '0' and int(a[2:]) >= 2:
        print("YES")
    else:
        print("NO")

