from collections import defaultdict


def solution(subway, start, end):
    path = defaultdict(set)

    for sub in subway:
        sub = list(map(int, sub.split(" ")))

        for i in range(len(sub) - 1):
            path[sub[i]].add(sub[i + 1])
        sub.reverse()
        for i in range(len(sub) - 1):
            path[sub[i]].add(sub[i + 1])

    paths = dfs_paths(path, start, end)

    transfer = 0
    # print(paths)
    # for p in paths:
    #     for ep in p:
    #         prev_num = num
    #         for num, sub in enumerate(subway):
    #             sub = list(map(int, sub.split(" ")))
    #             print(ep, ep in sub, num, sub)
    #             if num != prev_num
    print(paths)

    return len(paths)


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    result = []
    transfer = 0

    while stack:
        n, path = stack.pop()
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                stack.append((m, path + [m]))

    return result


solution(["1 2 3 4 5 6", "6 7 8", "1 2 3 4 5 6 7 8 9 10", "9 10"] , 1, 10)# → 최소환승 수)