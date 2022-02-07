from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def send_mssg(self, mssg):
        account_sid =YOUR_SID
        auth_token = YOUR_TOKEN
        client = Client(account_sid, auth_token)
        
        message = client.messages.create(
                                      body=mssg,
                                      from_=NUMBER,
                                      to=NUMBER
                                  )
        
