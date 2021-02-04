#importing twilio 
from twilio.rest import Client

#importing my secret everything from the twilio account
from my_secret_numbers import my_auth_token, my_cell_number

import pandas as Pd

account_sid = '91c'
auth_token = 'my_auth_token'

client = Client(account_sid, auth_token)

#sender and receiver details
sender = '+12075013401'

numbers = pd.read_csv('numbers.csv', names=['phone']).phone.tolist()[1:]
blacklist = pd.read_csv('blacklist.csv', names=['phone']).phone.tolist()[1:]

#numbers = [my_cell_number, my_cell_number]
#blacklist = ['+2608838838840']
receivers = list(set(numbers).difference(set(blacklist)))

for receiver in receivers:

#message
    text = 'Hey benjamin!'

    client.messages.create(to=receiver, from_=sender, body=text)

