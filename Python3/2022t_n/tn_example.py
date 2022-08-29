def solution(servers, sticky, requests):
    answer = [[] for _ in range(servers)]
    curr_server = 0
    req_to_server_id = {}

    for i, req in enumerate(requests):
        print(answer, req_to_server_id)

        if not sticky:
            answer[i % servers].append(req)
        else:
            if req in req_to_server_id:
                answer[req_to_server_id[req]].append(req)

            else:
                req_to_server_id[req] = curr_server
                answer[curr_server].append(req)
                curr_server = (curr_server+1) % servers

    return answer

#
# servers = 2
# sticky = False
# requests = [1, 2, 3, 4]
# result = solution(servers, sticky, requests)
# print(result)

# #########
# servers = 2
# sticky = True
# requests = [1, 2, 3, 4]
# result = solution(servers, sticky, requests)
# print(result)
# print(solution(2, True, [1,1,2,2]))

# print(solution(3, True, [1, 1, 3, 2, 1, 2, 3, 1]))
#
#
print(solution(3, True, [1,1,2,1,3,3,4]))
# 1114,2,33