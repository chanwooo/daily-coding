def solution(servers, sticky, requests):
    answer = [[] for _ in range(servers)]
    curr_server = 0
    req_to_server_id = {}

    for i, req in enumerate(requests):

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
