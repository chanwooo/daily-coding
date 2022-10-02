from collections import deque


def solution(n, m, sx, sy, gx, gy, k):
    maps = [[0 for _ in range(m)] for _ in range(n)]
    maps[gy][gx] = 1
    print(maps)
    answer = []

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y, k):
        path = ""
        queue = deque()
        queue.append((x, y))

        # queue가 빌 때까지 반복
        while queue and k != 0:
            print(maps)
            x, y = queue.popleft()

            # 상하좌우 칸 확인하기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                path+=i

                # 맵을 벗어나면 무시하기
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue

                # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))  # 재귀
                    k-=1


        # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[len(maps) - 1][len(maps[0]) - 1]

    answer = bfs(sx,sy, k)
    return answer

print(solution(3, 4, 2, 3, 3, 1, 5))  # dllrl
