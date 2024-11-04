def foo(text):
    answer = 0
    for s in text:
        if s in ["a", "e", "i", "o", "u"]:
            answer += 1

    return answer


print(foo("abracadabra"))
