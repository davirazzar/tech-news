import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
          url, headers={"user-agent": "Fake user-agent"}, timeout=3)
        if response.status_code != 200:
            return None
        html_content = response.text
        time.sleep(1)  # 1 seconds pause
    except requests.ReadTimeout:
        return None
    return html_content


# Requisito 2
def scrape_novidades(html_content):
    return (
      Selector(html_content).css(".entry-title a::attr(href)").getall()
    )


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
