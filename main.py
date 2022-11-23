from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from fastapi.middleware.cors import CORSMiddleware

import StockList

app = FastAPI()

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/plus/{a}/{b}")
async def plus(a: str, b: str):
    return {"res": a + b}


@app.get("/getRatio/{code}")
async def getRtnfromCode(code):
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
               # rate = rate[1:-1]
                res = float(rate[1].get_text().replace(',', ''))
            except:
                # 변동이 없는경우(검은글씨)
                rate = list(soup.select_one(".no_today > .X > .blind"))
                res = float(rate[1].get_text().replace(',', ''))
        return res


@app.get("/getStockPriceFromName/{name}")
async def getStockPriceFromName(name: str):
    global slp
    code = slp.getStockCode(name)
    return slp.getStockList(code).tolist()


slp = None
@app.on_event("startup")
async def onstart():
    global slp
    slp = StockList.StockListProvider()


@app.get("/getStockCode/{name}")
async def getStockCode(name: str):
    global slp
    return slp.getStockCode(name)