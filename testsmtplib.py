import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import string

#Initial Variables as Strings

email_user = 'personaldev99@gmail.com'

email_password = '3BRotherx'

email_send = "hamburger45.salama@gmail.com"

subject = "Testing"

#Starts MIMEMultipart email by declaring msg object.
msg = MIMEMultipart()
msg['From'] = email_user
msg["To"] = email_send
msg['Subject'] = subject
body = 'This is a test smtplib python automated email.'

#Attaches From, To, Subject and Body
msg.attach(MIMEText(body, 'plain'))

#Declares attachements filename
filename = "image.jpg"

#Instantiates MIMEBase Object
part = MIMEBase('application','octet-stream')

#Opens File
part.set_payload(open(filename, "rb").read())

#Encodes the attachment file, adds headers and attaches file.
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename= ' + str(filename))
msg.attach(part)

#Converts all the text and encoded attachement to a string in one variable.
text = msg.as_string()

#Starts SMTP Connection
server = smtplib.SMTP('smtp.gmail.com', 587)

#Says hello to server
server.ehlo()

#Starts encryption
server.starttls()

#Server Login
server.login(email_user, email_password)

#Custom built send method
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


