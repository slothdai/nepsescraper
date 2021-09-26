import scrapy
from bs4 import BeautifulSoup

class QuotesSpider(scrapy.Spider):
    name = "nepsebot"

    def start_requests(self):
        urls = [
            'http://merolagani.com/LatestMarket.aspx',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        trs = response.xpath("//tr").getall()[1:]
        for row in trs:
            data=[]
            for d in BeautifulSoup(row,"html.parser").find_all('td'):
                data.append(d.text)
            if (len(data)==0):
                return
            stock_data=dict()
            stock_data['Symbol']=data[0]
            stock_data['LTP']=data[1]
            stock_data['Change']=data[2]
            stock_data['High']=data[3]
            stock_data['Low']=data[4]
            stock_data['Open']=data[5]
            stock_data['Qty']=data[6]
            yield stock_data


