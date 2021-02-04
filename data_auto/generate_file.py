import static_data
 
import random

import datetime

import string

import os

def generate_reports(num):

	for current_num in range(num):

		file_name = str(current_num+1).zfill(3) + '_report.txt'

		f = open(file_name, 'w')

		date = str(datetime.date(2020,01,01) + datetime.timedelta(random.randint(1,365)))

		employee = random.choice(static_data.names)
		ongoing_tasks = '\t' + random.choice(static_data.ongoing_tasks) + '\n' + \
		                 '\t' + random.choice(static_data.ongoing_tasks) + '\n'
		completed_tasks = '\t' + random.choice(static_data.completed_tasks) + '\n' + \
                           '\t' + random.choice(static_data.completed_tasks) + '\n'
        problems = '\t' + random.choice(static_data.problems) + '\n' + \
                    '\t' + random.choice(static_data.problems) + '\n'
        approved_by = random.choice(static_data.names)

        report_content = 'BENJAMIN OFFICE REPORT\n\n' + \
                          'Date : '                      + date + '\n\n' + \
                          'Employee : '                  + employee + '\n\n' + \
                          'Ongoing Tasks : \n '          + ongoing_tasks + '\n' + \
                          'Completed Tasks : \n'         + completed_tasks + '\n' + \
                          'Problems : \n'                + problems + '\n' + \
                          'Approved By : '               + approved_by + '\n' 
                          
        f.write(report_content)

def generate_bloat(num):
	for current_num in range(num):
		file_name = str(random.randint(1,num)).zfill(3) + \
		          '_bloatfile_' + \
		          ''.join(random.choice(string.ascii_lowercase)) + \
		          '.txt'
		f = open(file_name, 'w')
		f.write('benjamin;)')

def delete_files():
	for file_name in os.listdir(os.getcwd()):
		if file_name.endswith('.txt'):
			os.remove(file_name)

delete_files()
generate_reports(10)
generate_bloat(5)