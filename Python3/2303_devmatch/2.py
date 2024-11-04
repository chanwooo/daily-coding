import sys

si = sys.stdin.readline
available = [list(map(int, si().split())) for _ in range(4)]

visit = [[False, False, False] for _ in range(4)]

ans = 0


def backtracking(x, y, length):
    global ans
    if length >= 2:
        ans += 1

    visit[x][y] = True

    dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < 4 and 0 <= ny < 3): continue
        if available[nx][ny] == 0: continue
        if visit[nx][ny]: continue

        backtracking(nx, ny, length + 1)

    visit[x][y] = False


for i in range(4):
    for j in range(3):
        if available[i][j] == 1:
            backtracking(i, j, 1)

print(ans)

# 1 1 1
# 1 1 1
# 1 1 1
# 1 1 1

# 193912


# 0 1 0
# 1 1 1
# 1 0 0
# 0 0 1
# => 96
