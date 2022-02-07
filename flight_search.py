import requests
from flight_data import FlightData

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self):
        self.atr='abc'
        self.url = 'https://tequila-api.kiwi.com'
        self.api = 'hoSJORYHE_GBTFLteUceTD6watBbxOwl'
        
    def get_iataCode(self, city):
        
        getUrl=self.url+'/locations/query'
        headers = {"apikey": self.api}
        query = {"term": city, "location_types": "city"}
        res=requests.get(url=getUrl, headers=headers, params=query)
        self.data=res.json()
        self.dataList=self.data['locations']
        return self.dataList[0]['code']
    
    def get_flightData(self,source, dest, from_date, to_date):
        
        getUrl=self.url+'/v2/search'
        headers = {"apikey": self.api}
        query={'fly_from':source,
               'fly_to':dest,
               'date_from':from_date.strftime("%d/%m/%Y"),
               'date_to':to_date.strftime("%d/%m/%Y"),
               'nights_in_dst_from': 7,
               'nights_in_dst_to': 28,
               'flight_type': 'round',
               'one_for_city': 1,
               'max_stopovers': 0,
               'curr':'GBP'}
        self.res=requests.get(getUrl, headers=headers, params=query)
        
        try:
            data = self.res.json()["data"][0]
        except IndexError:
            print(f"No flights found for {dest}.")
            return None 
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
    
    