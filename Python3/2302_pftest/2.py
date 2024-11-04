from collections import Counter


def stopWords(text, k):
    answer = []
    counter = Counter(text.split(" "))

    # print(counter)

    for word, count in counter.items():
        if count >= k:
            # print(word)
            answer.append(word)
    return answer

print(stopWords("the quick brown fox jumps over the lazy brown dog and runs away to a brown house", 2))
# print(stopWords("the brown fox jumps over the brown dog and runs away to a brown house", 2))
