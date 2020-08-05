from sys import setrecursionlimit
setrecursionlimit(10**9)
def dfs(x, y):
    if x == n-1 and y == m-1: return 1
    rtn = 0
    for d in range(4):
        i, j = x + dx[d], y + dy[d]
        if 0 <= i < n and 0 <= j < m and mountain[i][j] < mountain[x][y]:
            if visited[i][j] >= 0: rtn += visited[i][j]
            else:
                rtn += dfs(i, j)
    visited[x][y] = rtn
    return rtn
n, m = map(int, input().split())
mountain = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
visited[0][0] = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
print(dfs(0, 0))

