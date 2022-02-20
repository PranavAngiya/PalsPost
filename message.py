from twilio.rest import Client
from datetime import datetime
import schedule
import random,time

account_sid = 'ACa4ab73fc5a7ffcd2b7a372de70d037f7'
auth_token = '1db15bd1cb0cab96d554ff0904539ecd'
client = Client(account_sid, auth_token)
Twilio_num='+19035277600'
my_num='+14047544543'

Wake_Up = "As the ray of sun hits your eyes, you wake up to your pet lying on you. Your pet brings you a note. The note says:"

def send_message(Wake_Up):
    
    message = client.messages.create(
         body=Wake_Up,
         from_=Twilio_num,
         to=my_num
     )
    


time= "08:29:01"
time_two= "08:29:02"
check=False
schedule.every().day.at(time).do(send_message,Wake_Up)

while True:
    if check == False:
        if datetime.now().hour == int(time.split(':')[0]) and datetime.now().minute == int(time.split(':')[1]) and datetime.now().second == int(time.split(':')[2]):
            schedule.run_pending()
            check == True
        elif datetime.now().hour == int(time_two.split(':')[0]) and datetime.now().minute == int(time_two.split(':')[1]) and datetime.now().second == int(time_two.split(':')[2]):
            break


Morning_Quotes=["You are enough. You are strong, you can do anything you put your mind to."
,"Life isn't about finding yourself. Life is about creating yourself."
,"Success is not final, failure is not fatal: it is the courage to continue that counts."
,"What you're supposed to do when you don't like a thing is change it. If you can't change it, change the way you think about it. Don't complain."
,"Yesterday is history, tomorrow is a mystery, today is a gift of God, which is why we call it the present"]
quote=Morning_Quotes[random.randint(0,len(Morning_Quotes)-1)]

def send_message(quote):
    
    message = client.messages.create(
         body=quote,
         from_=Twilio_num,
         to=my_num
     )
    


time_three= "08:29:15"
time_four= "08:29:16"
check=False
schedule.every().day.at(time_three).do(send_message,quote)

while True:
    if check == False:
        if datetime.now().hour == int(time_three.split(':')[0]) and datetime.now().minute == int(time_three.split(':')[1]) and datetime.now().second == int(time_three.split(':')[2]):
            schedule.run_pending()
            check == True
        elif datetime.now().hour == int(time_four.split(':')[0]) and datetime.now().minute == int(time_four.split(':')[1]) and datetime.now().second == int(time_four.split(':')[2]):
            break



Interact = "If you want to interact with your pet, send any message to draw it's attention. "

def send_message(Interact):
    
    message = client.messages.create(
         body=Interact,
         from_=Twilio_num,
         to=my_num
     )

time_five= "08:29:30"
time_six= "08:29:31"
check=False
schedule.every().day.at(time_five).do(send_message,Interact)

while True:
    if check == False:
        if datetime.now().hour == int(time_five.split(':')[0]) and datetime.now().minute == int(time_five.split(':')[1]) and datetime.now().second == int(time_five.split(':')[2]):
            schedule.run_pending()
            check == True
        elif datetime.now().hour == int(time_six.split(':')[0]) and datetime.now().minute == int(time_six.split(':')[1]) and datetime.now().second == int(time_six.split(':')[2]):
            break