from typing import List


def foo(ids: List[int]) -> int:
    ids = list(set(ids))
    ids.sort()

    for idx, num in enumerate(ids):
        if idx != num:
            return idx

    return len(ids)


print(foo([0, 1, 1, 2, 7, 2, 3, 4, 5, 6]))
