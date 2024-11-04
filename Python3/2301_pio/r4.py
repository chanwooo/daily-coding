# 1 한글은 영문 2글자로 인식합니다.
# 2 새로운 줄의 첫글자는 빈칸이 될 수 없습니다.
# 3 영문기준 최대 80자로 한글이 포함된 경우 79자까지 표현할 수 있습니다. (81자 X)

from collections import deque


def foo(text):
    answer = ""
    buffer = deque(text)
    count = 0

    while buffer:
        char = buffer.popleft()

        # 1
        if len(char.encode()) > 1:
            count += 2
        else:
            count += 1

        # 2
        if char == " " and count == 1:
            char = ""
            count = 0

        answer += char

        # 3
        if count > 80:
            answer = answer[:-1]
            buffer.appendleft(char)
            answer += "\n"
            count = 0

    return answer


print(foo("이 글은 도커에 대해 1도 모르는 시스템 관리자나 서버 개발자를 대상으로 도커 전반에 대해 얕고 넓은 지식을 담고 있습니다. 도커가 등장한 배경과 도커의 역사, 그리고 도커의 핵심 개념인 컨테이너와 이미지에 대해 알아보고 실제로 도커를 설치하고 컨테이너를 실행해 보도록 하겠습니다."))
print(foo("벌써 옥 아스라히 토끼, 이네들은 새워 하나에 거외다. 걱정도 이름자를 묻힌 다 속의 계십니다. 하나에 동경과 다 강아지, 것은 계십니다. 이름을 계집애들의 부끄러운 어머니, 새겨지는 나는 이름과, 별에도 듯합니다. 써 다하지 새겨지는 사람들의 가난한 덮어 별 둘 했던 계십니다. 자랑처럼 가난한 같이 다 프랑시스 추억과 가득 이름과, 있습니다. 나는 그러나 어머니, 프랑시스 가난한 걱정도 까닭입니다. 별을 같이 위에도 별 묻힌 새겨지는 이름을 북간도에 아이들의 거외다. 헤일 그러나 언덕 계십니다. 위에도 우는 덮어 쓸쓸함과 까닭입니다. 청춘이 묻힌 하나에 하나에 노루, 하나에 많은 사랑과 어머님, 계십니다."))
