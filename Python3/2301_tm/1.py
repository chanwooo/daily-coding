def solution(numbers):
    answer = ""
    num_len = len(numbers)
    for i, num in enumerate(numbers):
        try:
            answer += bin(num)[2:].zfill(num_len)[num_len - i - 1]
        except IndexError:
            answer += "0"

    answer = answer[::-1]

    return int(answer, 2)


print(solution([5, 27, 9, 0, 31]))
