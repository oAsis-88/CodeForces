t = int(input())

for _ in range(t):
    n = int(input())
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))

    if a == b or a == tuple(reversed(b)):
        print("Bob")
    else:
        print("Alice")
