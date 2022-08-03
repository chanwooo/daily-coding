# https://school.programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    st = []
    for c in s:
        if len(st) == 0:
            st.append(c)
        elif st[-1] == c:
            st.pop()
        else:
            st.append(c)
    # print(st)
    return 1 if len(st) == 0 else 0


# case 1
assert 1 == solution("baabaa")

# case 2
assert 0 == solution("cdcd")
