#!/usr/bin/env python3
import os
import json
import requests

def get_json_from_description(descr, filename):
	descr_list = descr.split('\n')
	dict = {}
	dict['name'] = descr_list[0]
	dict['weight'] = int(descr_list[1].replace('lbs', '').strip())
	dict['description'] = descr_list[2]
	dict['image_name'] = filename
	return dict

if __name__ == '__main__':
	descr_dir = 'supplier-data/descriptions/'
	filelist = os.listdir(descr_dir)
	descriptions = [filename for filename in filelist if os.path.splitext(filename)[1] == '.txt']
	for filename in descriptions:
		with open(os.path.join(descr_dir, filename), 'r', encoding='utf-8') as file:
			description = file.read()
			generated_json = get_json_from_description(description, os.path.splitext(str(filename))[0] + '.jpeg')
			r = requests.post('http://35.239.69.142/fruits/', json=generated_json)

