#by jachermocilla@gmail.com

import requests
import json

class PCLSearchExtractor:
    api_endpoint = ''
    
    def __init__(self, api_ep):
        self.api_endpoint = api_ep
        
    def extract(self,path,scope):
        files = {'input':open(path,'rb')} 
        response = requests.post(self.api_endpoint+"/"+scope,files=files)
        print response.text.encode('ascii','ignore')




with open('../../pclsearch.json') as config_file:
    config = json.load(config_file)

extractor = PCLSearchExtractor(config['grobid_api_endpoint'])
#extractor.extract("test.pdf","processHeaderDocument") 
extractor.extract("test.pdf","processFulltextDocument") 
        
       
