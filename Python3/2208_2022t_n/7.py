# Hacked by Tcan
from itertools import combinations
import time

def solution(money, stocks):
    # print("@Sol1")

    answer = []
    for i in range(1, len(stocks)):
        for combo in combinations(stocks, i):
            # print(combo)
            if sum(map(lambda x: x[1], combo)) > money:
                continue
            else:
                answer.append(sum(map(lambda x: x[0], combo)))

    answer = max(answer) if answer else 0
    # print(answer)


    # def buy(index, curr_money, value):
    #     ...


def solution2(money, stocks):
    # print("@Sol2")
    answer = 0

    def buy_stock(index, buy_money, value):
        nonlocal answer

        # 모든 주식을 샀을때 or 돈이 毛 자랄 때
        if index == len(stocks) or buy_money + stocks[index][1] > money:
            answer = max(answer, value)
            return

        for next_index in range(index + 1, len(stocks) + 1):
            buy_stock(next_index, buy_money + stocks[index][1], value + stocks[index][0])

    for i in range(len(stocks)):
        buy_stock(i, 0, 0)

    print(answer)

start1 = time.time()
for _ in range(1):
    solution2(10, [[1, 1], [3, 5], [3, 5], [4, 9]])
    # solution(10, [[1, 1], [3, 5], [3, 5], [4, 9]])  # 6
    # solution(10, [[1, 1], [3, 5], [3, 5], [7, 9]])  # 8
    # solution(18, [[1, 1], [3, 5], [3, 5], [7, 9]])  # 11
    # solution2(1000, [[1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #                 [1, 1], [3, 5], [3, 5], [7, 9],
    #                 [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9]])
    # # N 16개 0.06초?
    # 20개 1.5초?
    # 21개 3초
    # 22개 6초?
    # 23개 12초?
    # 24개 24초?
    # solution(10, [[1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #               [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9]])
    # solution(30, [[1, 31]])  # 0
print(f"time : {time.time()-start1}")

start2 = time.time()
for _ in range(1):
    ...
    # solution2(10, [[1, 1], [3, 5], [3, 5], [4, 9]])  # 6
    # solution2(10, [[1, 1], [3, 5], [3, 5], [7, 9]])  # 8
    # solution2(18, [[1, 1], [3, 5], [3, 5], [7, 9]])  # 11
    # solution2(1000, [[1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #                  [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #                  [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #                  [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #                  [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #                  [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #                  [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #                  [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #                  [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #                  [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #                  [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #                  [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9]]) # N 96개에서 10초정도..
    # solution2(10, [[1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9],
    #                [1, 1], [3, 5], [3, 5], [7, 9], [1, 1], [3, 5], [3, 5], [7, 9]])
    # solution2(30, [[1, 31]])  # 0
print(f"time : {time.time()-start2}")
