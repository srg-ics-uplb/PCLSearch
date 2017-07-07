# -*- coding: utf-8 -*-

#
# Crawls the PCSC 2017 proceedings site.
# This should be used in an Scrapy project
# jachermocilla@gmail.com
#


import scrapy
import requests

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

class PCSCProcSpider(scrapy.Spider):
    name = 'pcscprocspider' #use this for crawl
    allowed_domains = ['https://sites.google.com']
    start_urls = ['https://sites.google.com/a/dcs.upd.edu.ph/csp-proceedings/pcsc-2017/']


#    rules = (Rule(SgmlLinkExtractor(), callback='parse_url', follow=False), )

#    def parse_url(self, response):
#        item = MyItem()
#        item['url'] = response.url
#        return item

    global download_file_from_google_drive
    global get_confirm_token
    global save_response_content

    def parse(self, response):
	extractor = LinkExtractor(allow_domains='drive.google.com')
        links = extractor.extract_links(response)
        i=1
        for link in links:
            print link.url
            tmp=str(link.url)
            data=tmp.split('/')
            print data[5]
            download_file_from_google_drive(data[5],str(i)+".pdf")		          
            i=i+1

    def download_file_from_google_drive(id, destination):
        URL = "https://docs.google.com/uc?export=download"

        session = requests.Session()

        response = session.get(URL, params = { 'id' : id }, stream = True)
        token = get_confirm_token(response)

        if token:
           params = { 'id' : id, 'confirm' : token }
           response = session.get(URL, params = params, stream = True)

        save_response_content(response, destination)

    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
	CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
	        if chunk: # filter out keep-alive new chunks
        	    f.write(chunk)

