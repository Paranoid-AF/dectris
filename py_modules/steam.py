import requests
from bs4 import BeautifulSoup
import urllib

SEARCH_URL = "https://store.steampowered.com/search/results?term={}&force_infinite=1&supportedlang=english&ndl=1"

def search_app_list(keyword: str) -> list[tuple[int, str]] :
    search_result: list[tuple[int, str]] = []

    req_keyword = urllib.parse.quote_plus(keyword)
    res = requests.get(SEARCH_URL.format(req_keyword))
    soup = BeautifulSoup(res.text, "html.parser")

    for item in soup.find_all("a", class_="search_result_row"):
        app_id = item.attrs["data-ds-appid"]
        app_name = item.find("span", class_="title").text
        search_result.append((int(app_id), app_name))

    return search_result
