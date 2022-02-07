from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def send_mssg(self, mssg):
        account_sid ='ACfb4ae8eb10265c8cce54fe1afa1ef67a'
        auth_token = '747eb166f683724ab8cee792ed756032'
        client = Client(account_sid, auth_token)
        
        message = client.messages.create(
                                      body=mssg,
                                      from_='+19033296495',
                                      to='+917874683021'
                                  )
        print(message.sid)