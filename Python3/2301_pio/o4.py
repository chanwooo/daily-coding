def foo(numbers):
    odd_count = 0
    even_count = 0
    odd_index = -1
    even_index = -1

    for i, num in enumerate(numbers.split()):
        if int(num) % 2 == 0:
            even_count += 1
            even_index = i + 1
        else:
            odd_count += 1
            odd_index = i + 1

    if even_count == 1:
        return even_index
    elif odd_count == 1:
        return odd_index
    else:
        raise ValueError("홀수나 짝수가 여러개 존재")


print(foo("2 4 7 8 10"))
print(foo("1 2 1 1"))
# print(foo("1 1 1 2 2"))
