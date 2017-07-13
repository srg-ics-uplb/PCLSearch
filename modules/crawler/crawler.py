import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector

class RedSpider(scrapy.Spider):
    name = "RedSpider"
    allowed_domains =['sites.google.com']
    #start_urls=['https://sites.google.com/a/dcs.upd.edu.ph/csp-proceedings/pcsc-2017']
    start_urls=[]

    def parse(self, response):
        extractor = LinkExtractor(allow_domains=['drive.google.com','docs.google.com','sites.google.com'])
        links = extractor.extract_links(response)
        for link in links:
            print "******URL: " + link.url

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(RedSpider,start_urls=['https://sites.google.com/a/dcs.upd.edu.ph/csp-proceedings/pcsc-2017'])
process.start() # the script will block here until the crawling is finished
