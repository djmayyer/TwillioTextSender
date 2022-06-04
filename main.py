from twilio.rest import Client 
 
account_sid = 'ACa36b6887f40ee196e9cb244cb6bd39b7' 
auth_token = '[d13df854b3e379ed3aaa90534d0111ef]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGf735a4482a0c8b8cd83033c44cc2dce4',  
                              body='test',    
                              to='+447342723791' 
                          ) 
 
print(message.sid)