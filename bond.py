import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/interestDetail.naver?marketindexCd=IRR_CALL"
response = requests.get(url)
if response.status_code == 200:
    html = response.text
    #print(html)
    soup = BeautifulSoup(html,'html.parser')
    rate = list(soup.select_one(".no_today > .no_down"))
    rate = rate[1:-1]
    res = ''
    for i in rate:
        res += i.get_text()
    res = float(res)
    print(res)