#by jachermocilla@gmail.com

import requests
import json
import os
import sys
from pymongo import MongoClient
import xml.etree.ElementTree as ET

class PCLSearchExtractor:
    api_endpoint = ''
    
    def __init__(self, api_ep):
        self.api_endpoint = api_ep
        
    def extract(self,url,path):
        header_ep = self.api_endpoint+"/processHeaderDocument"
        full_ep = self.api_endpoint+"/processFulltextDocument"
        references_ep = self.api_endpoint+"/processReferences"

 
        files = {'input':open(path,'rb')}
        response = requests.post(header_ep,files=files)
        headers = response.text.encode('ascii','ignore')

        files = {'input':open(path,'rb')}
        response = requests.post(full_ep,files=files)
        full = response.text.encode('ascii','ignore')

        files = {'input':open(path,'rb')}
        response = requests.post(references_ep,files=files)
        references = response.text.encode('ascii','ignore')
        
        #print response.text.encode('ascii','ignore')
        root = ET.fromstring(headers)
        title=u"notitle"
        abstract=u"noabstract"
        authors=[]

        for node in root.iter():
            #print str(node.tag)+"=="+ str(node.attrib)
            if str(node.tag) == '{http://www.tei-c.org/ns/1.0}titleStmt':
                t = node.find('{http://www.tei-c.org/ns/1.0}title') 
                if t is not None:
                    title=t.text
            #    elif str(node.tag) == '{http://www.tei-c.org/ns/1.0}abstract':
            #        p=node.find('{http://www.tei-c.org/ns/1.0}p');
            #        if p is not None:
            #            abstract=p.text

            #for author in root.findall('.//{http://www.tei-c.org/ns/1.0}author'):
            #    author_name=""
            #    for persName in author.findall('.//{http://www.tei-c.org/ns/1.0}persName'):
            #        for forename in persName.findall('.//{http://www.tei-c.org/ns/1.0}forename'):
            #            author_name=author_name+" "+forename.text
            #        surname = persName.find('{http://www.tei-c.org/ns/1.0}surname')        
            #        if surname is not None:
            #            author_name=author_name+" "+surname.text
            #        authors.append(author_name)

            #print extracted data data
        print title
        #print authors
        #print abstract.encode('ascii','ignore')

        if title is None:
            title="(Untitled)"
            
        inserter = 'http://express:3000/articles'
        response = requests.post(inserter,{'title':title,'url':url,'xml_headers':headers,'xml_full':full,'xml_references':references}) 


def extract_all():
    with open('../../pclsearch.json') as config_file:
        config = json.load(config_file)
    
    extractor = PCLSearchExtractor(config['extractor']['grobid_api_endpoint'])

    sources = config['sources']
    
    unprocessed = open("unproc.txt","w")

    for source in sources:
        source_type=source['type']
        source_name=source['name']
        source_year=source['year']
        spider_class=source['spider_class']
        start_url=source['start_url']

        download_path=config['pclsearch']['pdfs_root']+"/"+source_type+"/"+source_name+"/"+source_year
        print download_path


        with open(download_path+"/"+source_name+"-"+source_year+".map") as json_file:  
            data = json.load(json_file)
            for p in data['articles']:
                try:
                    extractor.extract(p['url'],p['path']) 
                    print "SUCCESS"
                except Exception:
                    print "FAILED"
                    unprocessed.write(p['path']+"\n")
                    sys.exc_clear()
        
#        for f in os.listdir(download_path):
#            if f.endswith(".pdf"):
#                fpath=os.path.join(download_path,f)
#                print "###Processing.."+fpath
#                try:
#                    extractor.extract(fpath,"processHeaderDocument") 
#                    #extractor.extract(fpath,"processFulltextDocument") 
#                    #extractor.extract(fpath,"processReferences") 
#                    print "SUCCESS"
#                except Exception:
#                    print "FAILED"
#                    unprocessed.write(fpath+"\n")
#                    sys.exc_clear()

    unprocessed.close()
        
extract_all()
