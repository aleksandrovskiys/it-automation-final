#!/usr/bin/env python3
import psutil
import shutil
import emails
import socket


def check_cpu():
	if psutil.cpu_percent(interval=1) > 80:
		return False
	return True

def check_hdd():
	if psutil.disk_usage('/').percent < 20:
		return False
	return True

def check_ram():
	mem = psutil.virtual_memory()
	THRESHOLD = 500 * 1024 * 1024
	if mem.available <= THRESHOLD:
		return False
	return True

def check_localhost():
	localhost = socket.gethostbyname('localhost')
	return localhost=="127.0.0.1"


def send_error_message(subject):
	sender = 'automation@example.com'
	recepient = 'student-00-1071babbf114@example.com'
	message = emails.generate_email(sender, recepient, subject,
		'Please check your system and resolve the issue as soon as possible.')
	emails.send_email(message)
	print('Message sent')

if __name__ == '__main__':
	if not check_cpu():
		send_error_message('Error - CPU usage is over 80%')
	if not check_hdd():
		send_error_message('Error - Available disk space is less than 20%')
	if not check_ram():
		send_error_message('Error - Available memory is less than 500MB')
	if not check_localhost():
		send_error_message('Error - localhost cannot be resolved to 127.0.0.1')
