import random


def solution(N, bus_stop):
    for stop_i, stop in enumerate(bus_stop):
        bus_stop[stop_i][0] -= 1
        bus_stop[stop_i][1] -= 1

    def calc_dist(row, col, visit_count, dist):
        if row < 0 or row >= N or \
                col < 0 or col >= N or \
                visited[row][col] >= visit_count + 1:
            return

        if answer[row][col] != 0:
            answer[row][col] = min(dist, answer[row][col])
        else:
            answer[row][col] = dist

        visited[row][col] += 1
        dist += 1


        print(dist)

        calc_dist(row + 1, col, visit_count, dist)
        calc_dist(row - 1, col, visit_count, dist)
        calc_dist(row, col + 1, visit_count, dist)
        calc_dist(row, col - 1, visit_count, dist)

    answer = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    stop_dict = {}
    for i in range(len(bus_stop)):
        stop_dict[i] = [bus_stop[i][0], bus_stop[i][1]]
    print(stop_dict)

    for i, stop in enumerate(stop_dict.values()):
        calc_dist(stop[0], stop[1], i, 0)

    print(answer)

    # return answer


# print(solution(3, [[1, 2]]))
print(solution(3, [[1, 2], [3, 3]]))
# print(solution(600, [[random.randrange(600), random.randrange(600)] for _ in range(10)]))
