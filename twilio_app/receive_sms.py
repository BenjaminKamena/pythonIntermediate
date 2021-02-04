
from flask import Flask

from twilio.twiml.messaging_response import MessagingResponse

web_app = Flask(__name__)

def sms_reply():

	automatic_response = MessagingResponse()

	automatic_response.message('Hello this an auto reply from python')

	return str(automatic_response)

web_app.add_url_rule('/sms', 'sms_reply', sms_reply, methods=['GET', 'POST'])


if __name__ == '__main__':
   
   web_app.run()