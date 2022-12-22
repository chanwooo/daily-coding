import re


def solution(files):
    files_dict = dict()
    for file in files:
        body = file.split(".")
        body = body[0]

        re_str = re.compile("\D+")
        head = re_str.findall(body)[0].lower()
        re_num = re.compile("\d+")
        number = re_num.findall(body)[0].rjust(5, '0')

        files_dict[file] = head + number

    print(files_dict.values())
    answer = sorted(files_dict, key=lambda key: files_dict[key])
    return answer


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# 기댓값 〉	["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]


print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# 기댓값 〉	["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]))

print(solution(["a 3", "a 22", "a 1"]))
