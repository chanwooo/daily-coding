def sol(nums, k):
    l = len(nums)

    prefix_sum = [0] * (l+1)

    # prefix_sum[0] = nums[0]

    for i in range(l):
        prefix_sum[i+1] = prefix_sum[i] + nums[i]

    for i in range(l+1):
        for j in range(i+1):
            ...


    print(prefix_sum)


def calc(nums, k):
    ...


# print(sol([2, 1, 3], 4)) # 3

print(sol([1, 2, 3, 4], 4))  # 3
# 1 2 3 4 ->  ps[1]-ps[0], ps[2]-ps[1], ps[3]-ps[2], ps[4]-ps[3]
# 12 23 34 -> ps[2]-ps[0], ps[3]-ps[1], ps[4]-ps[2]
# 123 234 -> ps[3]-ps[0], ps[4]-ps[1]
# 1234    -> ps[4]-ps[0]

# 1 2 3 3 4 5 5 6 7 9 10
