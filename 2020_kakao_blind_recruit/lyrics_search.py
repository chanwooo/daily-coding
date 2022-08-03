"""
[Programmers] 60060 - 가사 검색

https://programmers.co.kr/learn/courses/30/lessons/60060
2020 카카오 공채 코딩테스트 기출
"""
from collections import defaultdict


def insert(trie, word):
    curr = trie
    while word:
        s = word[0]
        if s not in curr:
            curr[s] = [0, {}]
        curr[s][0] += 1
        curr = curr[s][1]
        word = word[1:]


def find(trie, query):
    v = 0
    curr = trie
    while query:
        if query[0] == "?":
            return v
        else:
            if len(trie)==0 or query[0] not in curr:
                return 0
            v = curr[query[0]][0]
            curr = curr[query[0]][1]

        query = query[1:]
    return v


def solution(words, queries):
    trie = defaultdict(dict)
    rev_trie = defaultdict(dict)
    len_dict = defaultdict(int)
    ans = []

    for word in words:
        insert(trie[len(word)], word)
        insert(rev_trie[len(word)], word[::-1])
        len_dict[len(word)] += 1

    for q in queries:
        lq = len(q)

        if q[0] == "?" and q[-1] == "?":
            ans.append(len_dict[lq])
        elif q[-1] == "?":
            # ans.append(find(trie.get(lq, [lq, 0]), q))
            ans.append(find(trie[lq], q))
        elif q[0] == "?":
            # ans.append(find(rev_trie.get(lq, [lq, 0]), q[::-1]))
            ans.append(find(rev_trie[lq], q[::-1]))
        else:
            print("error")

    return ans


# [3, 2, 4, 1, 0]
w, q = ["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]

# w, q = ["frodo", "frozen","aaaaa"], ["a????"]
# w, q = ["ac"],["a?","?c","???"]

print(solution(w, q))
