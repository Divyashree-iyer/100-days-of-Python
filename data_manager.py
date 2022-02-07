
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        
        self.url = URL2SHEETY
        
    def get(self):
        self.res=requests.get(url=self.url)
        self.data=self.res.json()
        self.dataList=self.data['sheet1']
        return self.dataList
        
    
    def put(self, id, iataCode):
        putUrl=self.url+'/'+str(id)
        requests.put(url=putUrl, json={
                'sheet1':
                    {'iataCode':iataCode}
                })
    
