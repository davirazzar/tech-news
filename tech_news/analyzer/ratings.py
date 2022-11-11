from tech_news.database import search_news
from operator import itemgetter


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
    """Seu código deve vir aqui"""
