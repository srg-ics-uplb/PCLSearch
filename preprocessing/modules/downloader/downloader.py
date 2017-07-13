#by jachermocilla@gmail.com


import requests
import sys
import json

class PCLSearchDownloader:
    def download(self,url,target_path):
        pass

class GoogleDriveDownloader(PCLSearchDownloader):

    def download(self,url,target_path):
        download_url = "https://docs.google.com/uc?export=download"
        session = requests.Session()
        id = url.split('/')[5]
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


with open('../../pclsearch.json') as config_file:
    config = json.load(config_file)
print config['pclsearch']['pdfs_root']
downloader = GoogleDriveDownloader()
downloader.download("https://drive.google.com/file/d/0BxI8feCZhWsobHdYSWVJX0h5WGM/view",config['pclsearch']['pdfs_root']+"/test.pdf")
