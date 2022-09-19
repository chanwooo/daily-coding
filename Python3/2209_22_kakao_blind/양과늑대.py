answer = -1


def solution(info, edges):
    print(info, edges)
    # for i in range(len(info)):
    #     if info[i] == 0:
    #         info[i] = 1
    #     else:
    #         info[i] = -1

    graph = {node: [] for node in range(len(info))}

    for edge in edges:
        graph[edge[0]].append(edge[1])
    print(graph)

    # print(graph)

    def dfs(start_v, sheep, wolf, visit):
        sheep += info[start_v] ^ 1
        wolf += info[start_v]

        if sheep <= wolf:
            return
        if sheep > wolf:
            global answer
            answer = max(answer, sheep)

        for next in visit:
            print(visit)
            temp = set(graph.get(next, []))
            visit |= temp
            visit -= set([next])
            dfs(next, sheep, wolf, visit)
            print(visit)
            visit |= set([next])
            visit -= temp

        #
        # discovered = [start_v]
        # queue = [start_v]
        # while queue:
        #     v = queue.pop(0)
        #     for w in graph[v]:
        #         if w not in discovered:
        #             discovered.append(w)
        #             queue.append(w)
        # return discovered

    dfs(0, 0, 0, set(graph[0]))
    print(answer)
    return answer


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7],
                [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))  # 5

# print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
#                [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5],
#                 [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
