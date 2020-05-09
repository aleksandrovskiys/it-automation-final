#!/usr/bin/env python3
from email.message import EmailMessage
from os import path
import mimetypes
import smtplib

def generate_email(sender, recepient, subject, body, abs_path):
	basename = path.basename(abs_path)
	mimetype, _ = mimetypes.guess_type(abs_path)
	mimetype, mimesubtype = mimetype.split('/')

	message = EmailMessage()
	message['From'] = sender
	message['To'] = recepient
	message['Subject'] = subject
	message.set_content(body)
	with open(abs_path, 'rb') as attach:
	    message.add_attachment(attach.read(),
                           maintype=mimetype,
                           subtype=mimesubtype,
                           filename=basename)


def send_email(sender, mail_pass, message):
	mail_server = smtplib.SMTP_SSL('localhost')
	mail_server.connect()
	mail_server.set_debuglevel(1)
	res = mail_server.login(sender, mail_pass)
	print(res)
	mail_server.send_message(message)
	mail_server.quit()

if __name__ == '__main__':
	sender = 'automation@example.com'
	recepient = 'student-04-2cc6736db7e5@example.com'
	subject = 'Upload Completed - Online Fruit Store'
	body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
	abs_path = path.abspath('processed.pdf')
	message = generate_email(sender, recepient, subject, body, abs_path)
	print(message)
	send_email(sender, 'CB587ybqxZF', message)
