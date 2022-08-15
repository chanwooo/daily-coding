def solution(servers, sticky, requests):
    answer = [[] for _ in range(servers)]
    next_server = 0

    for i, req in enumerate(requests):
        print("====req", req, answer)

        if sticky:
            find = False
            # find
            for server_id in range(servers):
                if req in answer[server_id]:
                    answer[server_id].append(req)
                    next_server = (server_id + 1) % servers
                    find = True
                    print("-----find", req, server_id, next_server)

            # not find, add
            if not find:
                print("-not find", req, server_id, next_server)
                answer[next_server].append(req)
                next_server = (next_server + 1) % servers

        else:
            answer[i % servers].append(req)

    return answer


servers = 2
sticky = False
requests = [1, 2, 3, 4]
result = solution(servers, sticky, requests)
print(result)

##########
servers = 2
sticky = True
requests = [1, 2, 3, 4]
result = solution(servers, sticky, requests)
print(result)

print(solution(3, True, [1, 1, 3, 2, 1, 2, 3, 1]))
