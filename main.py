from twilio.rest import Client
import string
import random
import os

# put your own credentials here
account_sid = "ACa36b6887f40ee196e9cb244cb6bd39b7"
auth_token = "339e3a605ddd93d68a71d18b4c194ea4"

#Randomizer for 2FA
letters = string.digits
receiverVerificationCode = ''.join(random.choice(letters) for i in range(5))

#Client Constructor
client = Client(account_sid, auth_token)

receiverTextDraft = "Your Veriffication code is: "
receiverTextFinal = receiverTextDraft + receiverVerificationCode
#Message creator
message= client.messages.create(
    to="+447342723791",
    from_="+19472253535",
    body=receiverTextFinal
)

#MAIN
def main():
    code = input("Enter the code: ")
    if code == receiverVerificationCode:
        print("AuthentificatedSuccessfully!")
        
    else: print("Authentification Error")


if __name__ == "__main__":
    main()