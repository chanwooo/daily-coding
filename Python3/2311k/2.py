from collections import defaultdict


def solution(edges):
    # 정점, 도넛, 막대, 8자
    result = [0, 0, 0, 0]
    edge = defaultdict(list)
    for e in edges:
        edge[e[0]].append(e[1])

    for e in edge:
        if e in edge[e]:
            result[1] += 1

    print(result)



print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))

# print(solution(
#     [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2],
#      [7, 11], [4, 8], [9, 6], [10, 11], [6, 10],
#      [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))
