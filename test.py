import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    res = requests.get('https://finance.naver.com/item/sise.naver?code=005930')
    if res.status_code == 200:
        tmp = res.text
        soup = BeautifulSoup(tmp, 'html.parser')
        price = list(soup.find_all('span', 'tah p11'))
        for i in price:
            print(i.get_text().strip())
