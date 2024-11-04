from itertools import combinations
from itertools import product
from collections import defaultdict


#
# def solution(dice):
#     l_dice = len(dice)
#     vs = list(combinations(list(range(l_dice)), l_dice // 2))
#
#     # dice_set: win , draw, lose
#     dice_result = defaultdict(list)
#
#     count = 0
#
#     for i in range(l_dice):
#         a_dices_id = vs[i]
#         b_dices_id = vs[-i - 1]
#
#         print("a", a_dices_id, list(map(lambda x: dice[x], a_dices_id)))
#         print("b", b_dices_id, list(map(lambda x: dice[x], b_dices_id)))
#
#         for a in a_dices_id:
#             for b in b_dices_id:
#                 result = [0, 0, 0]
#
#                 for dice_a in dice[a]:
#                     for dice_b in dice[b]:
#                         count += 1
#                         print("dice_a_b", dice_a, dice_b, "count", count,
#                               "win" if dice_a > dice_b else "lose" if dice_a < dice_b else "draw")
#                         if dice_a > dice_b:
#                             result[0] += 1
#                         elif dice_a == dice_b:
#                             result[1] += 1
#                         else:
#                             result[2] += 1
#
#             dice_result[a_dices_id].append(result)
#
#         print(dice_result)
#         print(count)
#
#         return sorted(dice_result, key=lambda x: x[0])
def solution(dice):
    l_dice = len(dice)
    dice_result = defaultdict(list)

    vs = list(combinations(list(range(l_dice)), l_dice // 2))
    for i in range(l_dice):
        result = [0, 0, 0]

        a_dices_id = vs[i]
        b_dices_id = vs[-i - 1]
        print(a_dices_id, b_dices_id)
        a_dice = list(map(sum, product(*list(map(lambda x: dice[x], a_dices_id)))))
        # print(a_dice)
        # a_dice = sum(a_dice, [])
        b_dice = list(map(sum, product(*list(map(lambda x: dice[x], b_dices_id)))))
        # b_dice = sum(b_dice, [])
        # print(a_dice, b_dice)

        match = list(product(*[a_dice, b_dice]))
        for m in match:
            if m[0] > m[1]:
                result[0] += 1
            elif m[0] == m[1]:
                result[1] += 1
            else:
                result[2] += 1
        print(result)
        if result[2] > result[0]:
            result = [result[2], result[1], result[0]]
            dice_result[b_dices_id] = result
        else:
            dice_result[a_dices_id] = result

    print("Result")
    print(dice_result)
    dice_result = list(sorted(dice_result.items(), key=lambda x: x[1], reverse=True))
    print(dice_result)
    return list(map(lambda x: x + 1, list(list(dice_result[0])[0])))


print("=>", solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))

print("=>", solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]))

print("=>", solution([[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41],
                      [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]))

# print(solution([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 6, 5], [12, 12, 13, 15, 14, 62], [11, 2, 3, 5, 6, 41]]))
