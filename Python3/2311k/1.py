from collections import defaultdict


def solution(friends, gifts):
    gift_dict = defaultdict(list)
    gift_dict2 = defaultdict(list)
    gift_rate = defaultdict(int)

    gift_history = defaultdict(int)

    result = defaultdict(int)

    for gift in gifts:
        gift_history[gift] += 1
        gift = gift.split()
        gift_history[gift[1] + " " + gift[0]] -= 1
        gift_dict[gift[0]].append(gift[1])
        gift_dict2[gift[1]].append(gift[0])

    for k in friends:
        gift_rate[k] += len(gift_dict[k]) - len(gift_dict2[k])

    print("history", gift_history)
    print("gift1", gift_dict)
    print("gift2", gift_dict2)
    print("rate", gift_rate)

    for i in range(len(friends)):
        for j in range(len(friends)):

            if gift_history[friends[i]+" "+friends[j]] > 0:
                result[friends[i]] += 1
                print(friends[i], friends[j], "if1")

            if gift_rate[friends[i]] > gift_rate[friends[j]]:
                if not (gift_history[friends[i]+" "+friends[j]] or gift_history[friends[j]+" "+friends[i]]):
                    print(friends[i], friends[j], "if2")
                    result[friends[i]] += 1

    print("result", result)
    return max(result.values()) if result else 0


f, g = ["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi",
                                          "frodo muzi", "frodo ryan", "neo muzi"]
print(solution(f, g))
#
f, g = ["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
print(solution(f, g))

f, g =["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]
print(solution(f, g))
