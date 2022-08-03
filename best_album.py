"""
Programmers 42579 베스트앨범
https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3
"""


def solution(genres, plays):
    genre_rank = {}
    songs_by_genre = {}
    answer = []

    # for i, g, p in zip(range(len(genres)), genres, plays):
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_rank[g] = genre_rank.get(g, 0) + p
        songs_by_genre[g] = songs_by_genre.get(g, []) + [(p, i)]

    genre_rank = sorted(genre_rank.items(), key=lambda x: x[1], reverse=True)

    for g, p in genre_rank:
        songs_by_genre[g] = sorted(songs_by_genre[g], key=lambda x: (-x[0], x[1]))
        answer += [i for (p, i) in songs_by_genre[g][:2]]

    # return genre_rank, songs_by_genre, answer
    return answer


# result : [4, 1, 3, 0]
g, p = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]

# g, p = ["a","b","c","d","b"],[1,2,3,4,10]
print(solution(g, p))
