from collections import deque

def BFS(edges, c, u, visited):

    count = 0
    q = deque([])
    visited[u] = True

    for w in edges[u]:
        q.append(w)
        visited[w] = True
    while q:
        v = q.popleft()
        
        if c[v] == c[u]:
            count += 1
        else:
            for w in edges[v]:
                if not visited[w]:
                    visited[w] = True
                    q.append(w)
    return count  

t = int(input())

for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    edges = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges[u - 1].append(v - 1)
        edges[v - 1].append(u - 1)
    
    total_count = 0
    for u in range(n):
        visited = [False] * n
        total_count += BFS(edges, c, u, visited)
    
    print(total_count//2)