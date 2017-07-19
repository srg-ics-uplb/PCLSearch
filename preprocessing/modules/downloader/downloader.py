#by jachermocilla@gmail.com


import requests
import sys
import json

import os
import os.path

class PCLSearchDownloader:
    def download(self,url,target_path):
        pass

class GoogleDriveDownloader(PCLSearchDownloader):

    def download(self,url,target_path):
        if "open" in url:
                data=url.split('=')
                data=data[1].split('&')
                docid=data[0]
        elif "viewer" in url:
                data=url.split('=')
                docid=data[3]
        else:
                data=url.split('/')
                docid=data[5]

        print docid
        print target_path

        download_url = "https://docs.google.com/uc?export=download"
        session = requests.Session()
        id = docid
        response = session.get(download_url, params = { 'id' : id }, stream = True)
        token = self.get_confirm_token(response)
        if token:
           params = { 'id' : id, 'confirm' : token }
           response = session.get(URL, params = params, stream = True)
        self.save_response_content(response, target_path)

    def get_confirm_token(self,response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(self,response,target_path):
        CHUNK_SIZE = 32768
        with open(target_path, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)


def download_all():
    with open('../../pclsearch.json') as config_file:
        config = json.load(config_file)

    sources = config['sources']

    for source in sources:
        source_type=source['type']
        source_name=source['name']
        source_year=source['year']
        spider_class=source['spider_class']
        start_url=source['start_url']

        #source may require a different downloader later
        downloader=GoogleDriveDownloader()

        url_path_map = {}
        url_path_map['articles'] = []


        download_path=config['pclsearch']['pdfs_root']+"/"+source_type+"/"+source_name+"/"+source_year
        urls = download_path+"/"+source_name+"-"+source_year+".url"
        #print urls
        f = open(urls)
        i=-1
        for line in f:
            i = i+1
            if (i==0):
                continue
            else:
                #print line
                if os.path.exists(download_path+"/"+str(i)+".pdf"):
                    print ">>>Source in cache."
                else:
                    downloader.download(line,download_path+"/"+str(i)+".pdf")
                url_path_map['articles'].append({"url":line,"path":download_path+"/"+str(i)+".pdf"})
                 #print url_path_map

        with open(download_path+"/"+source_name+"-"+source_year+".map",'w') as outfile:  
            json.dump(url_path_map, outfile)
        
         


download_all()
