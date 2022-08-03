"""
https://programmers.co.kr/learn/courses/30/lessons/42628
[Programmers] 42628 - 이중우선순위큐
"""

import heapq


def solution(operations):
    max_heap = []
    min_heap = []

    for op in operations:
        o, v = op.split(' ')
        v = int(v)
        if o == "I":
            heapq.heappush(max_heap, -v)
            heapq.heappush(min_heap, v)

        elif o == "D":
            if v == 1:
                if max_heap:
                    heapq.heappop(max_heap)
                    # heapq.heappop(min_heap)
                    min_heap.pop()
            elif v == -1:
                if min_heap:
                    heapq.heappop(min_heap)
                    # heapq.heappop(max_heap)
                    max_heap.pop()

        print(max_heap, min_heap)

    if not (min_heap or max_heap):
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]]
