"""
https://programmers.co.kr/learn/courses/30/lessons/42629
[Programmers] 42629 - 라면공장
"""
import heapq


def solution(stock, dates, supplies, k):
    q = []
    supplied_count = 0
    start = 0

    while stock < k:
        for i in range(start, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(q, (-supplies[i], supplies[i]))
                start = i + 1
            else:
                break

        stock += heapq.heappop(q)[1]
        supplied_count += 1

    return supplied_count

if __name__ == '__main__':
    stock, dates, supplies, k = 4, [4, 10, 15], [20, 5, 10], 30
    # stock, dates, supplies, k = 3, [2, 4, 10, 15], [11, 100, 5, 10], 35
    print(solution(stock, dates, supplies, k))
