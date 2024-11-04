def foo(data):
    mid_value = sorted(data)[1]
    return data.index(mid_value)


print(foo([0, 1, 2]))
print(foo([5, 1, 2]))
