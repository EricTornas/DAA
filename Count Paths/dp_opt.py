from collections import defaultdict

def dfs(u, parent, colors, adj, fq):
    global count
    fq[u][colors[u]] = 1

    for v in adj[u]:
        if v == parent:
            continue
        dfs(v, u, colors, adj, fq)
        if len(fq[v]) > len(fq[u]):
            fq[v], fq[u] = fq[u], fq[v]  # swap de diccionarios
        for p in fq[v].items():
            count += fq[u].get(p[0], 0) * p[1]
            fq[u][p[0]] = fq[u].get(p[0], 0) + p[1]

        fq[u][colors[u]] = 1

t = int(input())
for _ in range(t):
    count = 0

    n = int(input())
    adj =  [[] for _ in range(n)]
    fq = [defaultdict(int) for _ in range(n)]
    colors  = list(map(int,input().split()))

    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    dfs(0, -1, colors, adj, fq)
    print(count)