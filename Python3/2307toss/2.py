# 친구관계인 1과 2, 2와 3이 있다면 1과 3을 친구로 인정하여 원래 알던 친구당 5원, 새롭게 알게 된 친구당 10원의 보상을 주는 기능입니다.
# 친구로 인정되는 최대 단계를 제한하여 보상금액을 조절하려합니다.


def solution(relationships, target, limit):
    graph = {}
    global newfriends
    global origfriends
    global result

    result = 0
    newfriends = 0
    origfriends = 0

    for a, b in relationships:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        if b not in graph:
            graph[b] = []
        graph[b].append(a)
    print(graph)

    def dfs(start, limit, visited, depth):
        global newfriends
        global origfriends
        global result

        print(visited, depth)
        if depth == 1:
            origfriends += 1
            result += 5
        else:
            newfriends += 1
            result += 10

        if depth == limit:
            return
        for i in graph[start]:
            if i not in visited:
                visited.append(i)

                dfs(i, limit, visited, depth + 1)
        return visited

    visit = dfs(target, limit, [target], 0)
    # visit.remove(target)
    # print(visit)
    # result += len(visit) * 10
    # result -= len(graph[target]) * 5
    # result += (len(visit) - len(graph[target]))

    # print(origfriends, newfriends)

    return result + newfriends


rel = [[1, 2], [2, 3], [2, 6], [3, 4], [4, 5]]
target = 2
limit = 2
result = solution(rel, target, limit)
print(result)
# result 37

print()
rel, t, l = [[1, 2], [2, 3], [2, 6], [3, 4], [4, 5]], 1, 1
print(solution(rel, t, l))
# 27
