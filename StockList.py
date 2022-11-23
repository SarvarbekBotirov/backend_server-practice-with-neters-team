import FinanceDataReader as fdr
import pandas as pd


class StockListProvider:
    def __init__(self):
        self.krx = pd.read_csv("krx.csv", encoding='euc-kr')
        self.res = {}
        tmp = self.krx.loc[:, ['name', 'code']]
        for i in range(len(tmp)):
            name = tmp.iloc[i].loc['name']
            code = tmp.iloc[i].loc['code']
            self.res[name] = str(code)
        print(self.res)

    def getStockList(self, code: str):
        res = fdr.DataReader(code).loc[:, 'Close']
        return res

    def getStockCode(self, name: str):
        try:
            tmp = self.res[name]
            cnt = 6 - len(tmp)
            for i in range(cnt):
                tmp = "0" + tmp
            return tmp
        except:
            return "000000"


if __name__ == "__main__":
    slp = StockListProvider()
    print(slp.getStockList("005930"))
    print(slp.getStockCode("삼성전자"))
    print(slp.getStockCode("삼성전지"))
