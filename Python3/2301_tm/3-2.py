def solution(N, bus_stop):
    answer = 0
    city_map = [[0 for _ in range(N)] for _ in range(N)]
    bus_map = [[False for _ in range(N)] for _ in range(N)]
    direction_list = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    queue = []
    visited = [[False] * N] * N

    for i in bus_stop:
        bus_map[i[0] - 1][i[1] - 1] = True

    def is_in(row, col):
        return 0 <= row < N and 0 <= col < N

    def find(row, col):
        while len(queue) > 0:
            q = queue.pop(0)

            if bus_map[q[0]][q[1]]:
                return abs(q[0] - row) + abs(q[1] - col)

            for d in direction_list:
                new_row = q[0] + d[0]
                new_col = q[1] + d[1]

                if is_in(new_row, new_col):
                    if not visited[new_row][new_col]:
                        visited[new_row][new_col] = True
                        queue.append([new_row, new_col])

    for row in range(N):
        for col in range(N):
            queue = []
            visited = [[False for _ in range(N)] for _ in range(N)] * N

            if bus_map[row][col]:
                city_map[row][col] = 0
                continue

            visited[row][col] = True
            queue.append([row, col])
            city_map[row][col] = find(row, col)

    for row in city_map:
        answer += sum(row)

    return city_map


# print(solution(3, [[1, 2]]))
# print(solution(3, [[1, 2], [3, 3]]))
import random
print(solution(100, [[random.randrange(100), random.randrange(100)]for _ in range(2)]))
