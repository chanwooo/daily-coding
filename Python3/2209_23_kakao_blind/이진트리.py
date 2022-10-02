def solution(numbers):
    answer = []
    bin_nums = []
    for num in numbers:
        bin_num = bin(num)[2::]
        if len(bin_num) % 2 == 0:
            bin_num = "0" + bin_num
        bin_nums.append(bin_num)

        for i, n in enumerate(bin_num):
            if i % 2 == 0 and n == '0':
                answer.append(0)
            else:
                answer.append(1)
                break

    return answer


# print(solution([7, 5])) #[1,0]
print(solution([127, 5]))  # [1,0]
