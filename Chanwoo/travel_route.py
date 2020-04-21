"""
https://programmers.co.kr/learn/courses/30/lessons/43164
[Programmers] 43164 - 여행경로
"""



def solution(tickets):
    routes = dict()
    st = ["ICN"]
    answer = []

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]

    for r in routes.keys():
        routes[r].sort(reverse=True)

    while st:
        top = st[-1]

        if top not in routes or len(routes[top])==0:
            answer.append(st.pop())
        else:
            st.append(routes[top][-1])
            routes[top] = routes[top][:-1]
        print(st)

    print(answer)
    return answer[::-1]







# t = 	[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# result = ["ICN", "JFK", "HND", "IAD"]


t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
# result = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(solution(t))