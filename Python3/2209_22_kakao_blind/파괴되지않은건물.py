def solution_time_fail(board, skill):
    # print(board)
    # print(skill)

    count = len(board) * len(board[0])
    # print(count)
    for s in skill:
        atck_heal = s[0]
        atck_heal = -1 if atck_heal == 1 else 1
        dmg = s[5]

        for r in range(s[1], s[3] + 1):
            for c in range(s[2], s[4] + 1):
                before = board[r][c]
                board[r][c] += dmg * atck_heal
                if before > 0 and board[r][c] < 1:
                    # print("destroy")
                    count -= 1
                if before < 1 and board[r][c] > 0:
                    # print("rebuild")
                    count += 1

    #
    # for r in range(len(board)):
    #     for c in range(len(board[0])):
    #         if board[r][c] > 0:
    #             count += 1

    return count


def solution(board, skill):
    global n, m
    n = len(board)
    m = len(board[0])
    skill_board = [[0] * (m + 1) for _ in range(n + 1)]
    skill_check(skill_board, skill)
    print(skill_board)

    answer = 0
    for r in range(n):
        for c in range(m):
            if skill_board[r][c] + board[r][c] > 0:
                answer += 1

    return answer


def skill_check(s_map, skill):
    for action in skill:
        action[0] = -1 if action[0] == 1 else 1
        degree = action[5]

        r1 = action[1]
        c1 = action[2]
        r2 = action[3]
        c2 = action[4]

        s_map[r1][c1] += degree * action[0]
        s_map[r1][c2 + 1] -= degree * action[0]
        s_map[r2 + 1][c1] -= degree * action[0]
        s_map[r2 + 1][c2 + 1] += degree * action[0]
        print(s_map)

    for r in range(n + 1):  # 행 기준 누적합
        for c in range(1, m + 1):
            s_map[r][c] += s_map[r][c - 1]

    for c in range(m + 1):  # 열 기준 누적합
        for r in range(1, n + 1):
            s_map[r][c] += s_map[r - 1][c]
    # return


print(solution([[5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4],
                [1, 2, 0, 2, 3, 2],
                [2, 1, 0, 3, 1, 2],
                [1, 0, 1, 3, 3, 1]]))  # 5
