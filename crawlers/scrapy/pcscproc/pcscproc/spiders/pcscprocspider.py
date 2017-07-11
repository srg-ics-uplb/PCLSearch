# -*- coding: utf-8 -*-

#
# Crawls the PCSC proceedings site.
# This should be used in an Scrapy project
# jachermocilla@gmail.com
#


import scrapy
import requests
import sys

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector


class PCSCProcSpider(scrapy.Spider):
    name = 'pcscprocspider' #use this for crawl
    allowed_domains = ['https://sites.google.com']
    start_urls=[
#		 'https://sites.google.com/a/dcs.upd.edu.ph/csp-proceedings/pcsc2012/',
#                'https://sites.google.com/a/dcs.upd.edu.ph/csp-proceedings/pcsc2013/',
#                'https://sites.google.com/a/dcs.upd.edu.ph/csp-proceedings/pcsc2014/',
#                'https://sites.google.com/a/dcs.upd.edu.ph/csp-proceedings/pcsc-2016/',
#                'https://sites.google.com/a/dcs.upd.edu.ph/csp-proceedings/pcsc-2015/',
                'https://sites.google.com/a/dcs.upd.edu.ph/csp-proceedings/pcsc-2017']
    
    #counter

    i = 1

    global download_file_from_google_drive
    global get_confirm_token
    global save_response_content
    global direct_download
    global extract_paper_headers

    def parse(self, response):
        extractor = LinkExtractor(allow_domains=['drive.google.com','docs.google.com'])
        links = extractor.extract_links(response)

        pdf_dir="/var/www/html/pdfs/"

        index_file=open("index.txt", "a+")

        for link in links:
            
            tmp=str(link.url)
            print "URL: " + tmp
            
            if ".pdf?att" in tmp:
                print "DIRECT DOWNLOAD"
                direct_download(link.url,str(self.i))          
                break
            elif "open" in tmp:
                data=tmp.split('=')
                data=data[1].split('&')
                docid=data[0]
            elif "viewer" in tmp:
                data=tmp.split('=')
                docid=data[3]
            else:
                data=tmp.split('/')
                docid=data[5]

            print docid
            
            path_name = pdf_dir+str(self.i)+".pdf"
            download_file_from_google_drive(docid,path_name)		          
            index_file.write(tmp +","+path_name+"\n")
            extract_paper_headers(docid, path_name)

            self.i = self.i+1

        index_file.close()
    def direct_download(url, destination):
        r = requests.get(url, stream=True)
        with open(destination, 'wb') as fd:
            for chunk in r.iter_content(chunk_size):
                fd.write(chunk)

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


    def extract_paper_headers(docid,path_name):
        try:
            url = 'http://grobid:8080/processHeaderDocument'
            files = {'input':open(path_name,'rb')}
            r = requests.post(url,files=files)
            print r.text
        except Exception:
            unprocessed = open("unproc.txt","a+")
            unprocessed.write(docid+","+path_name+"\n")
            unprocessed.close()
            sys.exc_clear()

