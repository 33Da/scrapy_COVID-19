from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# 根据项目配置获取 CrawlerProcess 实例
process = CrawlerProcess(get_project_settings())

# 添加需要执行的爬虫
process.crawl('world_spider')
process.crawl('China_spider')
process.crawl('china_citys_spider')

# 执行
process.start()