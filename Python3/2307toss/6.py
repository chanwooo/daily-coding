from itertools import combinations


def solution(prices, k):
    candi = list(combinations(prices, k + 1))
    result = []
    s = 0

    for c in candi:
        buy = c[0]
        for i in range(1, len(c)):
            s = sum(c[1:i + 1]) - buy * (len(c)-1)
            result.append(s)
    #     print(c, buy, s)
    # print(result)
    return max(result)


p, k = [10, 7, 8, 5, 8, 7, 6, 2, 9], 3
print(solution(p, k))
# 9

p, k = [10, 8, 6, 5, 7, 6, 4, 2, 1], 4
print(solution(p, k))
# -1

p,k = [10, 6, 5, 6, 7, 4, 3, 1, 10], 3
print(solution(p, k))
# 8

p, k = [44, 51, 44, 47, 47, 43, 40, 36, 35, 35, 30], 3
print(solution(p, k))
#13

p,k = [77, 89, 81, 75, 66, 73, 85, 89], 3
print(solution(p, k))
# 49
