"""
https://programmers.co.kr/learn/courses/30/lessons/42890
[Programmers] 42890 - 후보키
"""
def solution(relation):
    answer_list = list()
    # 순열을 만들기 위해 비트연산을 이용
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                # 이미 정답에 들어있는 컬럼과 겹친다면 그것은 중복임으로 제외
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)