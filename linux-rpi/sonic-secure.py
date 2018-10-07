from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import urllib.request
import smtplib
import time
import serial
import os

print('setting save directory')
path = os.getcwd()+'/pictures'

#seting serialinput
ser = serial.Serial(
    port='/dev/ttyUSB0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)

def test():
    #reading and testing serialinput
     for line in ser.read():
         if chr(line) == "1":
             print("motion detected!")
             send_mail()
             take_picture()

#send mail
def send_mail():
	
    # create message object instance
    msg = MIMEMultipart()
 
    subject = "sonic secure"
    message = "there is some one!"
 
    # setup the parameters of the message
    password = "password"
    msg['From'] = "email"
    msg['To'] = "email"
    msg['Subject'] = subject
 
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    #create serverhihh
    print("create server")
    server = smtplib.SMTP('smtp.gmail.com: 587')
 
    server.starttls()
 
    # Login Credentials for sending the mail
    print("Login Credentials for sending the mail")
    server.login(msg['From'], password)
 
    #send the message via the server
    print("send the message via the server")
    server.sendmail(msg['From'], msg['To'], msg.as_string())
 
    server.quit()
 
    print ("successfull sent email to %s=> " % (msg['To']) + message + '\n')

def take_picture():
    
    #get current path
    print('downloading')
    os.chdir(path)

    #remove old picture and download new picture
    def delp():
        os.remove("temp.jpg")
    def dowload():
        urllib.request.urlretrieve('frame of the ipcam''s stream', "temp.jpg")

    try:
        delp()
    except:
        dowload()

    dowload()


    print('done')

#main loop
while True:
    test()


ser.close()