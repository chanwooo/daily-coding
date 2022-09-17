from collections import defaultdict
def solution(invitationPairs):

    users = defaultdict(list)
    score = defaultdict(int)

    # 신규 +10
    # 아들 +3
    # 손자 +1

    for pair in invitationPairs:
        users[pair[0]].append(pair[1])
        score[pair[0]] += 10

        # print(pair)

    print()

    for pair in invitationPairs:
        # print(len(users[pair[1]]))
        score[pair[0]] += len(users[pair[1]])*3

    # for pair in invitationPairs:
    #     # score[pair[0]] += len(users[u])
    #     print(pair[0], users[pair[0]], users[pair[1]])

    for user in users:
        # print(user, users[user])
        for uu in users[user]:
            # print("-", user, users[uu])
            score[user] += len(users[uu])



    # for user in users:
    #     print(user, users[user])
    #     print(users[user])
    #     for u in users[user]:
    #         print(users[u])
    #     # score[user] += len(users[users[user][1]])*3
    #     print()


    print(users)
    print(score)
    # print()

    answer = sorted(score.items(), key=lambda x: x[1], reverse=True)
    answer = list(map(lambda x: x[0], answer))[:3]
    print(answer)

    return answer


solution([[1, 2], [3, 4]]) #13

solution([[1, 2], [1, 3], [3, 4], [4, 5], [4, 6], [4, 6]]) #413

solution([[1, 2], [2, 3], [2, 4], [2, 5], [5, 6], [5, 7], [6, 8], [2, 9]]) # 215