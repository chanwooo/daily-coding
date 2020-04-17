"""
현재 보유량 stock = 4
날짜 dates = [4, 10, 15]
공급량 supplies = [20, 5, 10]
일수 k = 30
"""

import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    start = 0
    max_heap = []

    while stock < k:
        for i in range(start, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(max_heap, -supplies[i])
                start = i + 1
            else:
                break
        stock += -heapq.heappop(max_heap)
        answer += 1

    return answer


print(solution(4, [4, 10, 15], [20, 5, 10], 30))