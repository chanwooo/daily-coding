import requests


def topArticles(limit):
    url = "https://jsonmock.hackerrank.com/api/articles"
    param = "?page="

    article_comment = dict()

    response = requests.get(url + param + "1")

    total_page = response.json()["total_pages"]

    for data in response.json()["data"]:
        if data["title"] and data["num_comments"]:
            article_comment[data["title"]] = data["num_comments"]
        elif data["story_title"] and data["num_comments"]:
            article_comment[data["story_title"]] = data["num_comments"]

    for i in range(2, total_page + 1):
        response = requests.get(url + param + str(i))

        for data in response.json()["data"]:
            if data["title"] and data["num_comments"]:
                article_comment[data["title"]] = data["num_comments"]
            elif data["story_title"] and data["num_comments"]:
                article_comment[data["story_title"]] = data["num_comments"]

    sorted_article_comment = sorted(article_comment, key=lambda key: (article_comment[key], key), reverse=True)
    return sorted_article_comment[:limit]


print(topArticles(5))
