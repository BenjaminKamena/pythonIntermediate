import os
import shutil

subdirectory_name = 'Flagged Files'

def process_all_reports():

	os.mkdir(subdirectory_name)

	for file_name in os.listdir(os.getcwd()):
		if file_name.endswith('_report.txt'):
			os.rename(file_name, file_name.lstrip())

			criteria = 'I don\'t want to automate with Python'
			criteria_met = search_for_criteria(file_name, criteria)

			if criteria_met == True:
				process_report(file_name)

def search_for_criteria(file_name, criteria):
	f = open(file_name)
	text_of_file = f.read()
	if criteria in text_of_file:
		return True
	else:

	   return False

def process_report(file_name):
	f = open(file_name)
	lines = f.readlines()
	for line in lines:
		if line.startswith('Employee:'):
			employee_for_review_1 = ' '.join(line.split()[1:])

		if line.startswith('Approved By: '):
			employee_for_review_2 = ' '.join(line.split()[2:])

	flagged_report_filename = "FLAGGED REPORT - " + employee_for_review_1 + ' .txt'
	flagged_report = open(flagged_report_filename, 'w')
	flagged_report.write("EMPLOYEES FLAGGED FOR REVIEW. CONSIDER TERMINATION. \n" + \
                          employee_for_review_1.upper() + \
                          'DOESN\'T WANT TO AUTOMATE WITH PYTHON\n' + \
                          employee_for_review_2.upper() + \
                          'APPROVED THIS.\n' + \
                          'COPY OF THE REPORT HERE:\n\n')

	f = open(file_name)
	flagged_report.write(f.read())
	os.rename(flagged_report_filename, os.path.join(subdirectory_name, flagged_report_filename))
    #return
def delete_file():
	if os.path.isdir(subdirectory_name):
		shutil.rmtree(subdirectory_name)


delete_file()
process_all_reports()