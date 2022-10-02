from itertools import product
from itertools import permutations


def solution(users, emoticons):
    print(users, emoticons)

    sale_rate = [0.1, 0.2, 0.3, 0.4]
    answer1 = 0
    answer2 = [[] for _ in range(len(users))]

    answer_candi = [[[0 for _ in range(4)] for _ in range(len(emoticons))] for _ in range(len(users))]

    for ui, (u_rate, u_price) in enumerate(users):
        for ei, emoticon in enumerate(emoticons):
            for ri, rate in enumerate(sale_rate):
                price = emoticon - emoticon * rate
                # if (u_rate / 100) <= rate:
                answer_candi[ui][ei][ri] = int(price)

    print(answer_candi)
    for ei, emoticon in enumerate(emoticons):
        for ui, (u_rate, u_price) in enumerate(users):
            for ri, rate in enumerate(sale_rate):
                # print("user", ui, "item", ei, "rate", rate, answer_candi[ui][ei][ri])
                if u_rate / 100 <= rate:
                    print(answer_candi[ui][ei], ui, rate)


    return answer1, answer2


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))  # [1, 5400]
# print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]
# )) # [4, 13860]
