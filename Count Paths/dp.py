from collections import defaultdict

def dfs(u, parent, colors, adj, fq):
    global count
    for v in adj[u]:
        if v != parent:
            dfs(v, u, colors, adj, fq)
    fq[u][colors[u] - 1] = 1
    for c in range(0, len(colors)):
        for v in adj[u]:
            if v != parent:
                if c == colors[u] - 1:
                    count += fq[v][c]
                else:
                    count += fq[v][c] * fq[u][c]
                    fq[u][c] += fq[v][c]

t = int(input())


for _ in range(t):
    count = 0
    n = int(input())
    colors = list(map(int, input().split()))
    fq = [[0] * len(colors) for _ in range(n)]
    adj = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    
    dfs(0, -1, colors, adj, fq)
    print(count)