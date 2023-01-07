from math import dist
from math import ceil


def solution(x, y):
    def find_next_island(curr, visit_count):
        if visit_count == len(islands):
            return

        min_dist = 10000
        min_island = None

        for i in range(len(visited)):
            if visited[i]:
                continue
            curr_dist = dist(islands[i], islands[curr])

            if min_dist > curr_dist:
                min_dist = curr_dist
                min_island = i

        min_dist_list.append(min_dist)
        visited[min_island] = True
        find_next_island(min_island, visit_count + 1)

    min_dist_list = []
    islands = {}

    for i in range(len(x)):
        islands[i] = [x[i], y[i]]

    visited = [False for _ in range(len(islands))]

    visited[0] = True
    find_next_island(0, 1)

    return ceil(max(min_dist_list))

print(solution([1, 2, 6, 8], [1, 2, 5, 7]))
