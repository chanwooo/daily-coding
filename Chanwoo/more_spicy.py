"""
https://programmers.co.kr/learn/courses/30/lessons/42626
Programmers 42626 더 맵게


"""

# import queue
import heapq


def solution(scoville, K):
    # pq = queue.PriorityQueue()
    heapq.heapify(scoville)
    count = 0

    while len(scoville) > 0:
        a = heapq.heappop(scoville)

        if a >= K:
            if count == 0:
                return -1
            else:
                return count

        if len(scoville) == 0:
            break

        b = heapq.heappop(scoville) * 2
        heapq.heappush(scoville, a + b)
        count += 1
    return -1


s, k = [1, 2, 3, 9, 10, 12], 7
# s, k = [1, 1, 1, 1, 1, 1], 100
# s, k = [1,2,3], 11
print(solution(s, k))
