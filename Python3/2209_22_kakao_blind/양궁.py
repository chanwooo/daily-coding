from itertools import combinations_with_replacement


def solution(n, info):
    info.reverse()
    result = []
    candi = []
    max_score = 0

    for shoot in combinations_with_replacement(range(11), n):
        ryan = [0] * 11
        for s in shoot:
            ryan[s] += 1

        res = calc_score(info, ryan)
        if res[0] > 0:
            candi.append(res)
            max_score = max(max_score, res[0])

    candi = sorted(candi, key=lambda x: (x[0], x[1]), reverse=True)

    for c in candi:
        if c[0] == max_score:
            print(list(reversed(c)))
            result.append(c[1])

    if len(result) == 0:
        return [-1]

    return list(reversed(result[0]))


def calc_score(apc, ryan):
    apc_score = 0
    ryan_score = 0
    for i, (a, r) in enumerate(zip(apc, ryan)):

        if a == r == 0:
            continue

        if a >= r:
            apc_score += i
        else:
            ryan_score += i

    # if ryan_score-apc_score > 0 :
    #     print(apc, ryan,apc_score, ryan_score, ryan_score-apc_score)
    return ryan_score - apc_score, ryan


# print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))  # [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]
# print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))  # [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))  # [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]
