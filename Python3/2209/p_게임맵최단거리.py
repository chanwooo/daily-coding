from collections import deque


def solution(maps):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    col_len, row_len = len(maps[0]) - 1, len(maps) - 1
    queue = deque([(0, 0, 1)])

    while queue:
        x, y, d = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx <= col_len and -1 < ny <= row_len:
                if maps[ny][nx] == 1 or maps[ny][nx] > d + 1:
                    maps[ny][nx] = d + 1
                    if nx == col_len and ny == row_len:
                        return d + 1

                    queue.append((nx, ny, d + 1))

    return -1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))  # 11
