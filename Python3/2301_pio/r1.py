def foo(month: int) -> int:
    if month in [1, 2, 3]:
        return 1
    elif month in [4, 5, 6]:
        return 2
    elif month in [7, 8, 9]:
        return 3
    elif month in [10, 11, 12]:
        return 4
    else:
        raise ValueError("month가 1~12가 아님")


print(foo(8))
