t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    queue = []
    bracket = 0
    count = 0
    for i in range(1, len(s), 2):
        if bracket == 0:
            bracket += 1
            queue.append('(')

        queue.append(s[i])
        if s[i] == ')':
            bracket -= 1
            queue.append('(')
        else:  # i == '('
            bracket += 1
            queue.append(')')

    queue.append(s[-1])

    q = []
    count = 0
    for i in range(len(queue)):
        if queue[i] == '(':
            q.append(i)
        else:
            count += i - q.pop()

    print(count - 1)
