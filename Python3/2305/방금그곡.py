from collections import defaultdict


def solution(m, musicinfos):
    class MusicInfo:
        def __init__(self, title, playtime, melody):
            self.title = title
            self.playtime = playtime
            self.melody = melody

        def __repr__(self):
            return f'MusicInfo(title={self.title}, playtime={self.playtime}, melody={self.melody})'

    def convert(m):
        conv = defaultdict(int)
        conv['A'] = 1
        conv['a'] = 2
        conv['B'] = 3
        conv['C'] = 4
        conv['c'] = 5
        conv['D'] = 6
        conv['d'] = 7
        conv['E'] = 8
        conv['F'] = 9
        conv['f'] = 10
        conv['G'] = 11
        conv['g'] = 12

        m = m.replace('A#', 'a')
        m = m.replace('C#', 'c')
        m = m.replace('D#', 'd')
        m = m.replace('F#', 'f')
        m = m.replace('G#', 'g')

        m = list(map(lambda x: conv[x], m))
        return m

    m = convert(m)

    print(m)

    musicinfo_list = []

    result = []

    for i in range(len(musicinfos)):
        title = musicinfos[i].split(',')[2]
        playtime = int(musicinfos[i].split(',')[1].split(":")[0]) * 60 - \
                   int(musicinfos[i].split(',')[0].split(":")[0]) * 60 + \
                   int(musicinfos[i].split(',')[1].split(":")[1]) - \
                   int(musicinfos[i].split(',')[0].split(":")[1])

        melody = convert(musicinfos[i].split(',')[3])

        if playtime > len(melody):
            melody = melody * (playtime // len(melody)) + melody[:playtime % len(melody)]
        else:
            melody = melody[:playtime]

        musicinfo_list.append(MusicInfo(title=title, playtime=playtime, melody=melody))

        if "".join(map(str, m)) in "".join(map(str, melody)):
            result.append((playtime, title))
    print(musicinfo_list)

    print(result)

    if len(result) != 0:
        result.sort(key=lambda x: (-x[0], x[1]))
        return result[0][1]
    else:
        return "(None)"


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
