answer = -1


def solution(info, edges):
    graph = {node: [] for node in range(len(info))}

    for edge in edges:
        graph[edge[0]].append(edge[1])

    def dfs(start_v, sheep, wolf, visit):
        sheep += info[start_v] ^ 1
        wolf += info[start_v]

        if sheep <= wolf:
            return
        if sheep > wolf:
            global answer
            answer = max(answer, sheep)

        for next in visit:
            temp = set(graph.get(next, []))
            visit |= temp
            visit -= set([next])
            dfs(next, sheep, wolf, visit)
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
    return answer


max_sheep = 0


class Node():
    def __init__(self, item):
        self.item = item
        self.right = None
        self.left = None
        self.parent = None

    def __repr__(self):
        """Return a string which when eval'ed will rebuild tree"""

        return '{}({}, {}, {})'.format(
            self.__class__.__name__,
            repr(self.item),
            repr(self.left) if self.left else None,
            repr(self.right) if self.right else None) \
            .replace(', None, None)', ')') \
            .replace(', None)', ')')

class BinaryTree():
    def __init__(self):
        self.root = None
    def __repr__(self):
        return self.root



def solution2(info, edges):
    tree = BinaryTree()
    nodelist = []
    for i in range(len(info)):
        nodelist.append(Node([i, info[i]]))
    for i in range(len(edges)):
        p, c = edges[i]
        if nodelist[p].left == None:
            nodelist[p].left = nodelist[c]
        else:
            nodelist[p].right = nodelist[c]
        nodelist[c].parent = nodelist[p]
    for i in range(len(nodelist)):
        if nodelist[i].parent == None:
            tree.root = nodelist[i]
    global max_sheep

    def dfs(cur, sheep, wolf, nex):
        global max_sheep
        if cur.item[1] == 0:
            sheep += 1
        if cur.item[1] == 1:
            wolf += 1
        #         print(cur.item, sheep, wolf, nex)
        if wolf >= sheep:
            return
        if max_sheep < sheep:
            max_sheep = sheep
        for i in range(len(nex)):
            if nex[i] != None:
                dfs(nex[i], sheep, wolf, nex[:i] + nex[i + 1:] + [nex[i].left, nex[i].right])
        return

    dfs(tree.root, 0, 0, [tree.root.right, tree.root.left])
    answer = max_sheep
    return answer

def solution3(info, edges):
    tree = BinaryTree()
    nodelist = []
    for i in range(len(info)):
        nodelist.append(Node([i, info[i]]))

    print(tree)

    for i in range(len(edges)):
        p, c = edges[i]
        if nodelist[p].left == None:
            nodelist[p].left = nodelist[c]
        else:
            nodelist[p].right = nodelist[c]
        nodelist[c].parent = nodelist[p]
    for i in range(len(nodelist)):
        if nodelist[i].parent == None:
            tree.root = nodelist[i]
    global max_sheep

    def dfs(cur, sheep, wolf, nex):
        global max_sheep
        if cur.item[1] == 0:
            sheep += 1
        if cur.item[1] == 1:
            wolf += 1
        #         print(cur.item, sheep, wolf, nex)
        if wolf >= sheep:
            return
        if max_sheep < sheep:
            max_sheep = sheep
        for i in range(len(nex)):
            if nex[i] != None:
                dfs(nex[i], sheep, wolf, nex[:i] + nex[i + 1:] + [nex[i].left, nex[i].right])
        return

    dfs(tree.root, 0, 0, [tree.root.right, tree.root.left])
    answer = max_sheep
    return answer

#
# print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#                [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7],
#                 [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))  # 5
#
# print(solution2([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#                 [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7],
#                  [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))  # 5

# print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
#                [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5],
#                 [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))


print(solution3([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7],
                [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))  # 5

