n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

def DFS(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and matrix[v][i] == 1:
            DFS(i)

def BFS(v):
    queue = [v]
    visit[v] = 0
    while (queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visit[i] == 1 and matrix[v][i] == 1:
                queue.append(i)
                visit[i] = 0

DFS(v)
print()
BFS(v)