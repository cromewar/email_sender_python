import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'User Name'
email['to'] = 'destinatary_email@gmail.com'
email['subject'] = 'Sample Subject'

email.set_content(html.substitute({'name' : 'Awesome Name'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('gmailaccount@gmail.com'), 'user_password')
    smtp.send_message(email)
    print('Email sent!')