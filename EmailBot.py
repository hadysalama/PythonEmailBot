import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time

print()
print("Hello welcome to the Python Email Bot 1.0")
print("Loading...")
print()
time.sleep(3)


while True:
    print()
    print("Select the option from the list below:")
    print("Option 1: Send Email")
    print("Option 2: Quit")
    option = int(input())
    if option == 2:
        break

    print()
    print("Please enter the SMTP address.")
    address = str(input())
    print()

    print("Please enter the server port.")
    port = int(input())
    print()

    print("Please enter your email address.")
    email_user = str(input())
    print()

    print("Please enter your email account password")
    email_password = str(input())
    print()

    print("Please enter your recepients email address.")
    email_send = str(input())
    print()

    print("Please enter the subject of your email.")
    subject = str(input())
    print()

    print("Please type out the body of your email.")
    text = str(input())
    print()

    print("Enter the name of the file you want to attach and make sure it is in the root directory")
    filename = str(input())
    print()

    print("How many times do you want to send this email")
    count = int(input())
    print()

    #Starts MIMEMultipart email by declaring msg object.
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg["To"] = email_send
    msg['Subject'] = subject
    body = text

    #Attaches From, To, Subject and Body
    msg.attach(MIMEText(body, 'plain'))

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
    server = smtplib.SMTP(address, port)

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

    for i in range(count):
        send()
        print("Email #" + str(i + 1))



    #closes connection
    server.close()

print()
print("Goodbye!")