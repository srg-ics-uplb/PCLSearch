import scrapy
import json
from scrapy.crawler import CrawlerProcess
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector

from pprint import pprint

import os
import os.path


class RedSpider(scrapy.Spider):
    name = "RedSpider"
    allowed_domains =['sites.google.com']
    start_urls=[]
    download_path=''

    def parse(self, response):
        extractor = LinkExtractor(allow_domains=['drive.google.com','docs.google.com','sites.google.com'])
        links = extractor.extract_links(response)
        filename=response.url.split("/")
        print "######"+self.download_path
        f = open(self.download_path,"w+")
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

    sources = config['sources']
        
    process = CrawlerProcess({
        'USER_AGENT': '/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
                
    for source in sources:
        source_type=source['type']
        source_name=source['name']
        source_year=source['year']
        spider_class=source['spider_class']
        start_url=source['start_url']

        download_path=config['pclsearch']['pdfs_root']+"/"+source_type+"/"+source_name+"/"+source_year
        print "*******"+download_path

        if config['pclsearch']['check_cache']:
            if os.path.exists(download_path+"/"+source_name+"-"+source_year+".url"):
                print ">>>Source in cache."
            else:
                if not os.path.exists(download_path):
                    os.makedirs(download_path)

                start_urls=[]
                start_urls.append(start_url)
                process.crawl(eval(spider_class),start_urls=start_urls,download_path=download_path+"/"+source_name+"-"+source_year+".url")


    process.start() # the script will block here until the crawling is finished

crawl_all()
