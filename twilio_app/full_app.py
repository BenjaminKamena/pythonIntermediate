#importing twilio 
from twilio.rest import Client

from flask import Flask, request

from twilio.twiml.messaging_response import MessagingResponse

#importing my secret everything from the twilio account
from my_secret_numbers import my_auth_token, my_cell_number

import pandas as pd

account_sid = 'A81c'
auth_token = 'my_auth_token'

client = Client(account_sid, auth_token)

#sender and receiver details
sender = '+12075013401'

numbers = pd.read_csv('numbers.csv', names=['phone']).phone.tolist()[1:]
blacklist = pd.read_csv('blacklist.csv', names=['phone']).phone.tolist()[1:]

#numbers = [my_cell_number, my_cell_number]
#blacklist = ['+260964115840']
receivers = list(set(numbers).difference(set(blacklist)))

def broadcast():

	import time
	time.sleep(100)

    for receiver in receivers:

         #message
         text = 'Hey benjamin!'

         client.messages.create(to=receiver, from_=sender, body=text, media_url='')




web_app = Flask(__name__)

def sms_reply():

	if request.method == 'POST':
		number = request.form['From']
		message_body = request.form['Body']


	if message_body == 'Y':
		response_text = ''

	if message_body == 'B':
		blacklist.append(number)
		df = pd.DataFrame(blacklist, columns=['phone'])
		df.to_csv('blacklist.csv', index=False)
		response_text = 'You have been blacklisted from the list'


	automatic_response = MessagingResponse()

	automatic_response.message(response_text)

	return str(automatic_response)

web_app.add_url_rule('/sms', 'sms_reply', sms_reply, methods=['GET', 'POST'])


if __name__ == '__main__':
   
   broadcast()
   web_app.run()