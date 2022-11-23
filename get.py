import requests
from bs4 import BeautifulSoup


def getRtnfromCode(code):
    url = "https://finance.naver.com/item/main.naver?code=" + code
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup.select_one(".no_today > .no_up"))
        try:  # down인 경우 (파란글씨)
            rate = list(soup.select_one(".no_today > .no_down"))
            print(rate)
            res = float(rate[1].get_text().replace(',', ''))
        except:
            try:  # up인 경우(빨간글씨)
                rate = list(soup.select_one(".no_today > .no_up"))
                rate = rate[1:-1]
                res = float(rate[1].get_text().replace(',', ''))
            except:
                # 변동이 없는경우(검은글씨)
                rate = list(soup.select_one(".no_today > .X > .blind"))
                res = float(rate[1].get_text().replace(',', ''))
        return res
