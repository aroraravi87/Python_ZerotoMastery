import smtplib

from email.message import EmailMessage
from string import Template
from pathlib import Path

#make sure less secure setting open should be on.

def send():
    
    html=Template(Path('documents/mailtemplate.html').read_text())
    
    email=EmailMessage()
    email['from']='Test user'
    email['to']='abc@gmail.com' # whom to send email

    email['subject']='hur..rah.. You won $10000 in jackpot lottery!!'

    email.set_content(html.substitute({'amount':'$10000','name':'Lucky'}))

    print(email)

    with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('yourusername','pssword') # your gmail user name and password to login account.
        smtp.send_message(email)
        print('All done!!!')
