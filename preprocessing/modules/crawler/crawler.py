import scrapy
import json
from scrapy.crawler import CrawlerProcess
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector

from pprint import pprint

class RedSpider(scrapy.Spider):
    name = "RedSpider"
    allowed_domains =['sites.google.com']
    start_urls=[]

    def parse(self, response):
        extractor = LinkExtractor(allow_domains=['drive.google.com','docs.google.com','sites.google.com'])
        links = extractor.extract_links(response)
        filename=response.url.split("/")
        f = open(filename[6]+".url","w+")
        f.write("=== "+response.url+"\n")
        for link in links:
            if 'drive.google' in link.url:
                f.write(link.url+"\n")
            elif 'docs.google' in link.url:
                f.write(link.url+"\n")
        f.close()    




def crawl_all():
    with open('../../pclsearch.json') as config_file:
        config = json.load(config_file)

    pprint(config)

    pcsc = config['sources']['conference']['pcsc']
        
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
                
    for item in pcsc:
        year=item['year']
        spider_class=item['spider_class']
        start_url=item['start_url']

        start_urls=[]
        start_urls.append(start_url)
        process.crawl(eval(spider_class),start_urls=start_urls)


    process.start() # the script will block here until the crawling is finished

crawl_all()
