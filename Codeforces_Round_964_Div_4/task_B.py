t = int(input())

for i in range(t):
    a1, a2, b1, b2 = map(int, input().split())

    if min(a1, a2) > min(b1, b2) and min(a1, a2) >= max(b1, b2):
        print(4)
    elif max(b1, b2) > min(a1, a2) > min(b1, b2) and max(a1, a2) >= max(b1, b2):
        print(2)
    else:
        print(0)

"""
b b a a  4
b ba a   4
b baa    4

b a b a  2
b a ab   2

b a a b  0
ba a b   0
a b a b  0
a ba b   0
a a b b  0

3 8 2 6
"""
