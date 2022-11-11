from tech_news.database import search_news
from collections import Counter


# Requisito 10
def top_5_news():
    database_result = search_news({})
    database_result.sort(key=lambda x: x.get('title'))
    database_result.sort(key=lambda x: x.get('comments_count'), reverse=True)
    result = []
    for news in database_result:
        if news:
            result.append((news["title"], news["url"]))
    return result[:5]


# Requisito 11
def top_5_categories():
    database_result = search_news({})
    result = []
    for news in database_result:
        if news:
            result.append(news["category"])
    result.sort()
    most_common_categories = Counter(result).most_common(5)
    top_5 = []
    for categorie in most_common_categories:
        if categorie:
            top_5.append(categorie[0])
    return top_5
