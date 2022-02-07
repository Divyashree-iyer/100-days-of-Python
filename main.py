#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

dataManager=DataManager()
sheet_data=dataManager.get()

flightSearch=FlightSearch()

notificationManager = NotificationManager()


for d in sheet_data:
    if d['iataCode']=='':
        iataCode=flightSearch.get_iataCode(d['city'])
        d['iataCode']=iataCode
        
    dataManager.put(d['id'], d['iataCode'])      
 
source='LON'    
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


for destination in sheet_data:
    flight = flightSearch.get_flightData(
        source,
        destination["iataCode"],
        from_date=tomorrow,
        to_date=six_month_from_today
    )

    if flight != None and flight.price < destination["lowestPrice"]:
        mssg=f'We have found a flight for you from {flight.origin_city} to {flight.destination_city} ! The price is {flight.price} Departure Airport Code is {flight.origin_airport} and Arrival Airport Code is {flight.destination_airport}. Departure is on {flight.out_date} and return date is {flight.return_date}'
        
        notificationManager.send_mssg(mssg)
        
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        