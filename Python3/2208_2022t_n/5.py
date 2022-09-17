from collections import defaultdict


def solution(tasks):
    answer = 0
    data = defaultdict(int)

    for task in tasks:
        data[task] += 1

    # 2 3 4 5 6 7 8 9 10 11 12 13
    print(dict(data))
    for item in data.values():
        if item == 1:
            print(-1)
            return -1

        if item % 3 == 0:
            answer += item // 3
        # elif item % 3 == 1:
        #     answer += item // 3 - 1 + 2
        else:
            answer += item // 3 + 1

    print(answer)
    return answer


def solution_using_list(tasks):
    answer = 0
    count = 0

    tasks.sort()
    tasks.append("-")

    for i in range(1, len(tasks)):
        count += 1

        if tasks[i - 1] != tasks[i]:
            if count == 1:
                return -1

            if count % 3 == 0:
                answer += count // 3
            else:
                answer += count // 3 + 1

            count = 0

    return answer


print(solution_using_list([1, 1, 2, 3, 3, 2, 2]))

# solution([1, 1, 2, 3, 3, 2, 2])  # 3
# solution([4, 1, 1, 1, 1, 2, 3])  # -1
# solution([1, 1, 2, 2])  # 2 -> 2 2
# solution([1, 1, 1, 1, 1, 2, 2])  # 3 -> 3 2 2
# solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])  # 4 -> 3 3 3 2
# solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])  # 5
# solution([1 for _ in range(111)]) # 37

# 2,3으로 만들수있는 수 중에 가장 작은거
