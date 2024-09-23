t = int(input())
A = []
dp = [0] * t
for _ in range(t):
    a, b, h = map(int, input().split())
    ring = (a, b, h)
    A.append(ring)

A.sort(key=lambda x: (x[1], x[0]), reverse=True)
max_val = A[0][2]
dp[0] = max_val
for i in range (1, t):
    aux = 0
    for j in range(t-1, -1 , -1):
        if A[i][1] > A[j][0] and dp[j] > aux:
            aux = dp[j]
    dp[i] = aux + A[i][2]    
    if dp[i] > max_val:
        max_val = dp[i] 
print(max_val)