from collections import defaultdict, Counter


def solution(N, stages):
    # curr_stage = defaultdict(int)
    curr_stage = Counter(stages)
    user_count = len(stages)
    fail_rate = defaultdict(float)

    # for stage in stages:
    #     curr_stage[stage] += 1
    print(curr_stage)

    for i in range(1, N + 1):
        if curr_stage[i] == 0:
            fail_rate[i] = 0
        else:
            fail_rate[i] = curr_stage[i] / user_count
            user_count -= curr_stage[i]

    # fail_rate = sorted(fail_rate.items(), key=lambda item: item[1], reverse=True)
    # result = []
    # for f in fail_rate:
    #     result.append(f[0])

    result = sorted(fail_rate, key=lambda key: fail_rate[key], reverse=True)
    return result

# N, M
# O(M + N + NlogN + N) -> O(N log N)
# n = 5, m = 8
# 8+5+5+5 = 23?
#
# N <= 500
# M <=200000
# O(200000+500+ 9*500 + 500) => 205500 -> O(M)

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4, 4, 4, 4, 4]))
# print(solution(2, [1, 1, 4]))
