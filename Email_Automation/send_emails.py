import smtplib

from email.mime.text import MIMEText

import email.utils

#put your email address
sender_email = 'benj9@gmail.com'

#put your name
sender_name = 'benja'

#put your own password
password = 'Ben94'

#this where your put your reciepient
recipient_emails = ['ben@gmail.com', 'unthu@gmail.com']
recipient_names = ['benjaminkamena ', ' benjaminkamena']

#the message to send
email_html = '''

<p><strong><span style="background-color: #0000ff;">letter from God</span></strong></p>
<p>Good afternoon Benjamin</p>
<p>Am sending this email to let you know that things are just like that sometimes thay become harder that you even think of committing suceide. But not to worry next week is your your weekyou look back and start pleasing me i have love your God</p>
<p>next week is your week to open doors</p>
<p><a href="https://www.shutterstock.com/search/heaven"><img src="https://www.shutterstock.com/image-photo/peaceful-heavenly-background-light-heaven-staircase-757721221" alt="my heaven" width="100" height="100" /></a></p>
<p>have a blessed day</p>
<p>with love from heaven</p>
<p>&nbsp;</p>

'''

def broadcast_email():

	print('\n Broadcasting email....\n')

	for recipient_name, recipient_email in zip(recipient_names, recipient_emails):

	     message = MIMEText(email_html, 'html')
	     message.add_header('Content-Type', 'text/html')

	     message['To'] = email.utils.formataddr((recipient_name, recipient_email))
	     message['From'] = email.utils.formataddr((sender_name, sender_email))
	     message['Subject'] = 'NOT SPAM. I CAN HELP YOU. NOT SPAM'

	     server = smtplib.SMTP('smtp.gmail.com', 587)

	     server.starttls()

	     server.login(sender_email, password)

	     server.sendmail(sender_email, recipient_email, message.as_string())

	     server.quit()

	     print(' Sent to ' + recipient_name + ' at ' + recipient_email)

	print('\n Email broadcasted..\n')

broadcast_email()
