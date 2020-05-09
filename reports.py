#!/usr/bin/env python3
import os
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(fruits_list):
	report = SimpleDocTemplate("processed.pdf")
	styles = getSampleStyleSheet()
	report_title = Paragraph("Processed Update on {}".format(datetime.today().strftime('%Y-%m-%d')), styles["h1"])
	report_body = "<br/>"
	for fruit in fruits_list:
		report_body += r"name: {}<br/>weight: {}<br/><br/>".format(fruit['name'], fruit['weight'])
	body_paragraph = Paragraph(report_body, styles['Normal'])
	report.build([report_title, body_paragraph])


if __name__ == '__main__':
	descr_dir = 'supplier-data/descriptions/'
	filelist = os.listdir(descr_dir)
	descriptions = [filename for filename in filelist if os.path.splitext(filename)[1] == '.txt']
	generated_list = []
	for filename in descriptions:
		with open(os.path.join(descr_dir, filename), 'r', encoding='utf-8') as file:
			description = file.read()
			descr_list = description.split('\n')
			generated_list.append({'name': descr_list[0], 'weight': descr_list[1]})
	generate_report(generated_list)
