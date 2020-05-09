#!/usr/bin/env python3
import requests
import os


if __name__ == "__main__":
	url = 'http://localhost/upload/'
	image_dir = 'supplier-data/images'
	filelist = os.listdir(image_dir)
	images = [filename for filename in filelist if os.path.splitext(filename)[1] == '.jpeg']
	for filename in images:
		with open(os.path.join(image_dir, filename), 'rb') as opened_file:
			r = requests.post(url, files={'file': opened_file})
