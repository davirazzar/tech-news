from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {'title': {'$regex': title, '$options': 'i'}}
    database_result = search_news(query)
    result = []
    for news in database_result:
        if news:
            result.append((news["title"], news["url"]))
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
