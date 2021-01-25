import scrapy
import time
import json
from ..items import *
import datetime
class StocksSpider(scrapy.Spider):
    name = 'world_spider'
    allowed_domains = ['view.inews.qq.com']
    start_urls = ['https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoforeignList']

    def parse(self, response):

        yiqing_json = json.loads(response.text)

        data = yiqing_json["data"]["FAutoforeignList"]

        for d in data:
            yiqing_item = WorldItem()
            yiqing_item["name"] = d["name"]
            yiqing_item["confirmAdd"] = d["confirmAdd"]
            yiqing_item["nowConfirm"] = d["nowConfirm"]
            yiqing_item["continent"] = d["continent"]
            yiqing_item["suspect"] = d["suspect"]
            yiqing_item["dead"] = d["dead"]
            yiqing_item["heal"] = d["heal"]

            yiqing_item["crawl_date"] = d["y"] + "." + d["date"]

            # 当前时间
            yiqing_item["crawl_date"] = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())


            yield yiqing_item







