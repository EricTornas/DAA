from collections import deque
t = int(input())
A = []
for _ in range(t):
    a, b, h = map(int, input().split())
    ring = (a, b, h)
    A.append(ring)

A.sort(key=lambda x: (x[1], x[0]), reverse=True)
q = deque([])
max_val = A[0][2]
height_q = 0

for i in range (0, t):
    while True:
        if len(q) == 0 or q[-1][0] < A[i][1]:
            q.append(A[i])
            height_q += A[i][2]
            break
        else:
            x = q.pop()
            height_q -= x[2]
    if height_q > max_val:
        max_val = height_q

print(max_val)