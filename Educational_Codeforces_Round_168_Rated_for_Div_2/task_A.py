t = int(input())

for _ in range(t):
    s = input()

    chars = set(chr(i) for i in range(97, 123)) - set(s)
    for c in range(2, len(s)):
        if s[c - 1] == s[c]:
            print(s[:c] + chars.pop() + s[c:])
            break
    else:
        print(s[0] + chars.pop() + s[1:])
