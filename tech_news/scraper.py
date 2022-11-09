import re
import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)  # 1 seconds pause
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code != 200:
            return None
        html_content = response.text
    except requests.ReadTimeout:
        return None
    return html_content


# Requisito 2
def scrape_novidades(html_content):
    return Selector(html_content).css(".entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_url = selector.css(
        "div.nav-links a.next.page-numbers::attr(href)"
    ).get()
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    page_info = {}
    page_info["url"] = selector.css(
        "head link[rel=canonical]::attr(href)"
    ).get()
    page_info["title"] = selector.css("h1.entry-title::text").get().strip()
    page_info["timestamp"] = selector.css(
        "ul.post-meta li.meta-date::text"
    ).get()
    page_info["writer"] = selector.css(
        "ul.post-meta span.author a.url.fn.n::text"
    ).get()
    page_info["comments_count"] = selector.css(
        "div#comments h5.title-block::text"
    ).get()
    if page_info["comments_count"] is None:
        page_info["comments_count"] = 0
    else:
        # https://pythonexamples.org/python-regex-extract-find-all-the-numbers-in-string/#:~:text=Python%20Regex%20%E2%80%93%20Get%20List%20of,single%20digit%20in%20the%20string.
        str = page_info["comments_count"]
        extract_number_regex = re.findall("[0-9]+", str)
        page_info["comments_count"] = extract_number_regex[0]
    page_info["summary"] = "".join(
        selector.css("div.entry-content > p:nth-of-type(1) *::text").getall()
    ).strip()
    print(page_info["summary"])
    page_info["tags"] = selector.css(
        "section.post-tags ul li a[rel=tag]::text"
    ).getall()
    page_info["category"] = selector.css(
        "div.entry-details div.meta-category a.category-style span.label::text"
    ).get()
    return page_info


# Requisito 5
def get_tech_news(amount):
    ...
    # URL_BASE = "https://blog.betrybe.com/"
    # next_page_url = "/page/1/"
    # news = []
    # while next_page_url:
    #     # Busca o conteúdo da próxima página
    #     html_content = fetch(URL_BASE + next_page_url)
    #     # Transforma o conteudo da página em um dict
    #     page_info = scrape_noticia(html_content)
    #     news.append(page_info)
    #     # Descobre qual é a próxima página
    #     next_page_url = scrape_next_page_link(html_content)
    # return news
