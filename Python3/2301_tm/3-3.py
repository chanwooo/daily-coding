def solution(N, bus_stop):
    city_map = [[-1 for _ in range(N)] for _ in range(N)]
    direction_list = [[0, -1], [0, 1], [1, 0], [-1, 0]]

    def is_in(x, y):
        return 0 <= x < N and 0 <= y < N

    def find(queue, dist, empty_count):
        print(dist)
        for r in city_map:
            print(r)

        if empty_count <= 0:
            return

        new_set = set()

        while queue:

            x, y = queue.pop()

            if city_map[x][y] < 0:
                city_map[x][y] = dist
                empty_count -= 1

            for d_x, d_y in direction_list:
                new_x = x + d_x
                new_y = y + d_y

                if is_in(new_x, new_y):
                    if city_map[new_x][new_y] < 0:
                        new_set.add((new_x, new_y))

        find(list(new_set), dist + 1, empty_count)

    for bs in bus_stop:
        bs[0] -= 1
        bs[1] -= 1

    print(bus_stop)
    find(bus_stop, 0, N*N)

    print()
    for row in city_map:
        print(row)


import random
import sys

sys.setrecursionlimit(2000)

# solution(600, [[random.randrange(600), random.randrange(600)] for _ in range(10)])
solution(5, [[random.randrange(5) + 1, random.randrange(5) + 1] for _ in range(2)])

# solution(5, [[5, 5], [1, 1], [4, 5], [4, 4]])
