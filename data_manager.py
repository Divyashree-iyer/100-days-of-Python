
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        
        self.url = 'https://api.sheety.co/0427e10ce9456848a20da460c2810e5f/flightSearch39/sheet1'
        
    def get(self):
        self.res=requests.get(url=self.url)
        self.data=self.res.json()
        self.dataList=self.data['sheet1']
        return self.dataList
        #print(self.res.json())
        #print("response.status_code =", self.res.status_code)
        #print("response.text= ", self.res.text)
    
    def put(self, id, iataCode):
        putUrl=self.url+'/'+str(id)
        requests.put(url=putUrl, json={
                'sheet1':
                    {'iataCode':iataCode}
                })
    