"""
"aa.jpg, London, 2022.12.11 22:10:33
ab.jpg, London, 2020.12.11 21:10:33
bb.jpg, London, 2019.12.11 21:11:33
aaa.png, London, 2018.12.13 20:09:33
aaa.png, Seoul, 2022.12.12 21:16:03"
=>
London4.jpg
London3.jpg
London2.jpg
London1.png
Seoul1.png

입력문자열을 적절히 파싱해서..처리해서 리턴하기
날짜순으로 파일명에 숫자를 붙임, 같은 도시에서 10개가 넘어가면 Taipei01.jpg
입력순서대로 문자열 리턴
"""


def sol(data:str)->str:

    for p in data.split("\n"):
        print(p)

    return "r"

print(sol("aa.jpg, London, 2022.12.11 22:10:33\n\
ab.jpg, London, 2020.12.11 21:10:33\n\
bb.jpg, London, 2019.12.11 21:11:33\n\
aaa.png, London, 2018.12.13 20:09:33\n\
aaa.png, Seoul, 2022.12.12 21:16:03"))


