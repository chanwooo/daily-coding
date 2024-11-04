# import permutation
from itertools import product
from itertools import combinations


def solution(schedules):
    schedules_with_index = list(enumerate(schedules))

    if len(schedules_with_index) % 2 == 0:
        candilen = len(schedules_with_index) // 2
    else:
        candilen = len(schedules_with_index) // 2 + 1
    candi = list(combinations(schedules_with_index, candilen))
    cc = []

    for c in candi:
        flag = False

        for i in range(len(c)):
            for j in range(i + 1, len(c)):
                if c[i][0] + 1 == c[j][0]:
                    print(c[i], c[j])
                    flag = True
                    break

        if not flag:
            cc.append(c)

    print(candi)

    print("cc=", cc)
    result = []

    for c in cc:
        result.append(sum(map(lambda x: x[1], c)))
        print(c, sum(map(lambda x: x[1], c)))

    return max(result)


s = [30, 30, 60, 90, 60, 15, 15, 60]
print(solution(s))
# 210
s = [60, 15, 60, 90, 45]
print(solution(s))
165
s = [30, 90, 30, 30, 30, 75, 75]
print(solution(s))
# 195
s = [15, 45, 90, 15, 90, 60]
print(solution(s))
# 195
