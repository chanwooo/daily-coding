from collections import defaultdict


def solution(N, A, B):
    path = defaultdict(set)

    for a, b in zip(A, B):
        path[a].add(b)
        path[b].add(a)
    print(path)

    paths = dfs_paths(path, 1, N)

    print(paths)
    print(list(range(1, N + 1)))
    # if list(range(1, N+1)) in paths:
    #     return True
    # else:
    #     return False

    for i in range(2, N + 1):
        if i - 1 not in path[i]:
            return False
    return True


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    result = []

    while stack:
        n, path = stack.pop()
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                stack.append((m, path + [m]))

    return result


print(solution(4, [1, 2, 1, 3], [2, 4, 3, 4]))
print(solution(4, [1, 2, 4, 4, 3], [2, 3, 1, 3, 1]))
print(solution(3, [1, 3], [2, 2]))
#     paths = dfs_paths(path, start, end)
#
#     convfer = 0
#     # print(paths)
#     for p in paths:
#         for ep in p:
#             prev_num = num
#             for num, sub in enumerate(subway):
#                 sub = list(map(int, sub.split(" ")))
#                 print(ep, ep in sub, num, sub)
#                 if num != prev_num
#
#     return len(paths)
#
#
