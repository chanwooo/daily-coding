#
# [0,1,2,3,4,5,6,7,8,9]
# [6,2,5,5,4,5,6,3,7,6]

# 2 : 1
# 3 : 7
# 4 : 4
# 5 : 2,3,5
# 6 : 0,6,9
# 7 : 8


# 성냥개비 K개로 만들 수 있는 숫자의 갯수
# k = 6
# 2,3,5

from itertools import combinations_with_replacement, permutations


def solution(k):
    # my_dict = {2:[1],3:[7],4:[4],5:[2,3,5],6:[0,6,9],7:[8]}
    my_dict = {2: 1, 3: 1, 4: 1, 5: 3, 6: 3, 7: 1}

    card = [2, 3, 4, 5, 6, 7]
    candi = []
    for i in range(8, k//2+1):
        for com in combinations_with_replacement(card, i):
            # print(com,sum(com))
            # for c in permutations(com):
            #     print(c, sum(c))
            if sum(com) == k:
                candi.append(com)

    # print(candi)
    # candi = set(candi)

    answer = 0

    for c in candi:
        # print(c, sum(c))
        temp = 1
        for e in c:
            temp *= my_dict[e]
        # print(temp)
        answer += temp

    # print(answer)

    print(max(candi,key=len),len(max(candi, key=len)))
    return answer

# print(solution(7)) #8?
# print(solution(8))
# print(solution(5)) # 5
# print(solution(6)) # 7
# print(solution(7))
# print(solution(11))  # 99
# print(solution(1)) # 0
# print(solution(7))

print(solution(50))
