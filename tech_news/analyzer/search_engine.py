from tech_news.database import search_news
from datetime import datetime


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
    try:
        datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")
    d = datetime.strptime(date, "%Y-%m-%d").strftime('%d/%m/%Y')
    query = {'timestamp': d}
    database_result = search_news(query)
    result = []
    for news in database_result:
        if news:
            result.append((news["title"], news["url"]))
    return result


# Requisito 8
def search_by_tag(tag):
    query = {'tags': {'$in': [tag.title()]}}
    database_result = search_news(query)
    result = []
    for news in database_result:
        if news:
            result.append((news["title"], news["url"]))
    return result


# Requisito 9
def search_by_category(category):
    query = {'category': {'$regex': category, '$options': 'i'}}
    database_result = search_news(query)
    result = []
    for news in database_result:
        if news:
            result.append((news["title"], news["url"]))
    return result
