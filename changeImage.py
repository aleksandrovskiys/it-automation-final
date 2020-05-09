#!/usr/bin/env python3
from PIL import Image
import os

if __name__ == "__main__":
	home_dir = os.path.expanduser('~')
	image_dir = os.path.join(home_dir, 'supplier-data/images')
	for infile in os.listdir(image_dir):
		filename, ext = os.path.splitext(infile)
		if ext == '.tiff':
			im = Image.open(os.path.join(image_dir, infile))
			converted = im.convert('RGB')
			converted.resize((600, 400))
			converted.save(os.path.join(image_dir, filename + '.jpg'), 'JPEG', quality=100)
