n, m = map(int, input().split())
matrix = []
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    matrix.append(list(input()))

queue = [[0, 0]]
matrix[0][0] = 1
while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and matrix[x][y] == "1":
            queue.append([x, y])
            matrix[x][y] = matrix[a][b] + 1

print(matrix[n - 1][m - 1])