from collections import defaultdict


def solution(phone):
    pos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    path = defaultdict(list)

    def make_path(r, c):
        dr = [-1, -1, 0, 1, 1, 1, 0, -1]
        dc = [0, 1, 1, 1, 0, -1, -1, -1]

        for d_r, d_c in zip(dr, dc):
            if (0 > r + d_r or r + d_r > 3) or (0 > c + d_c or c + d_c > 2):
                continue

            if phone[r + d_r][c + d_c] == 0:
                path[pos[r][c]].append(pos[r + d_r][c + d_c])

    for i in range(len(phone)):
        for j in range(len(phone[0])):
            if phone[i][j] == 0:
                make_path(i, j)

    print(path)


# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[1, 0, 1],
                [1, 0, 1],
                [1, 1, 0],
                [1, 0, 0]]))
