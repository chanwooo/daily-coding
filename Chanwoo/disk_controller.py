"""
https://programmers.co.kr/learn/courses/30/lessons/42627
[Programmers] 42627 - 디스크 컨트롤러
"""
import heapq


def solution(jobs):
    N = len(jobs)
    count = 0
    time = 0
    end_time = -1
    wait = []
    answer = []

    while count < N:
        for job in jobs:
            if end_time < job[0] <= time:
                answer.append(time - job[0])
                heapq.heappush(wait, job[1])
                print(time, end_time)
                print(job)
                print(answer,wait)

        if wait:
            answer.append(len(wait)*wait[0])
            end_time = time
            time += heapq.heappop(wait)
            count += 1
        else:
            time += 1
        print(answer, wait)
        print()

    # print(sum(answer)//N)
    return sum(answer)//N

if __name__ == '__main__':
    j = [[0, 3], [1, 9], [2, 6]]
    # j = [[0, 1], [2, 3], [4, 5]]  # 1 + 3 + 5 = 3
    # j = [[1,3],[5,2],[10,3]]

    # 74
    # j = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]

    # 74
    # j = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]

    # j = [[0, 3], [1, 9], [500, 6]] #6
    # j = [[0,3],[0,1],[4,7]]

    print(solution(j))
