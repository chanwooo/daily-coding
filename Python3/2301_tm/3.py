import random


def solution(N, bus_stop):
    def calc_dist(curr, target):
        return abs(curr[0] - target[0]) + abs(curr[1] - target[1])

    def calc_min(row, col):
        min = 10000
        for stop_i, stop in enumerate(bus_stop):
            if city[stop_i][row][col] < min:
                min = city[stop_i][row][col]
        return min

    city = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(len(bus_stop))]

    for stop_i, stop in enumerate(bus_stop):
        bus_stop[stop_i][0] -= 1
        bus_stop[stop_i][1] -= 1

    for stop_i, stop in enumerate(bus_stop):
        for row in range(N):
            for col in range(N):
                city[stop_i][row][col] = calc_dist([row, col], bus_stop[stop_i])
        # print(city[stop_i])

    answer = [[0 for _ in range(N)] for _ in range(N)]

    for row in range(N):
        for col in range(N):
            answer[row][col] = calc_min(row, col)

    return answer


# print(solution(3, [[1, 2]]))
print(solution(3, [[1, 2], [3, 3]]))
print(solution(60, [[random.randrange(60), random.randrange(60)]for _ in range(60)]))
