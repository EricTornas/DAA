from collections import defaultdict

def dfs(u, par=-1):
    global ans
    fq[u][col[u]] = 1

    for v in adj[u]:
        if v == par:
            continue

        dfs(v, u)

        if len(fq[v]) > len(fq[u]):
            fq[v], fq[u] = fq[u], fq[v]  # swap de diccionarios

        for p in fq[v].items():
            ans += fq[u].get(p[0], 0) * p[1]
            fq[u][p[0]] = fq[u].get(p[0], 0) + p[1]

        fq[u][col[u]] = 1



t = int(input())
for _ in range(t):
    ans = 0
    n = int(input())
    adj =  [[] for _ in range(n)]
    fq = [defaultdict(int) for _ in range(n)]
    col  = list(map(int,input().split()))
        

    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    
    dfs(0)
    print(ans)