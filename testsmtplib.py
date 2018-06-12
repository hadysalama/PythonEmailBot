import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import string


email_user = 'personaldev99@gmail.com'

email_password = '3BRotherx'

email_send = "hamburger45.salama@gmail.com"

subject = "Testing"

msg = MIMEMultipart()
msg['From'] = email_user
msg["To"] = email_send
msg['Subject'] = subject
body = 'This is a test smtplib python automated email.'

msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

filename = "image.jpg"

part = MIMEBase('application','octet-stream')
part.set_payload(open(filename, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename= ' + str(filename))

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()

#Starts encryption

server.starttls()

server.login(email_user, email_password)

def send():
    try: 
        server.sendmail(email_user, email_send, text)
        print()
        print('Email Sent!')
    except:
        print()
        print('Email not sent :(')

for i in range(1):
    send()
    print("Email #" + str(i + 1))



#closes connection
server.close()


