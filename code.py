
# -----------------------------------------------
# Resources
# -----------------------------------------------


# -----------------------------------------------
# Libraries
# -----------------------------------------------

import csv
import codecs


# -----------------------------------------------
# Functions
# -----------------------------------------------

def open_codecs(encoding_name):
	with codecs.open(file_in, "r", encoding=encoding_name) as fi:
		fi_csv = csv.reader(fi, delimiter=delimiter_in, quotechar=quotechar_in)
		header_line = next(fi_csv)
		with open(file_out,'w') as fo:
			fo_csv = csv.writer(fo,delimiter=delimiter_out, quotechar=quotechar_out)
			fo_csv.writerow(header_line)
			for row in fi_csv:
				if fi_csv.line_num % (1/sample_percent)  == 0:
					fo_csv.writerow(row)
			print('SUCCESSFUL: '+str(encoding_name)+' codecs.open')


# -----------------------------------------------
# Parameters
# -----------------------------------------------

file_in = 'input.csv'
delimiter_in = ','
quotechar_in = '"'

file_out = 'output.txt'
delimiter_out = '\t'
quotechar_out = '"'

sample_percent = 1
# e.g. 0.1 returns 10 percent of the full document (every 10th row)



# -----------------------------------------------
# Body
# -----------------------------------------------

try:
	open_codecs("utf-8")
except:
	print('UNSUCCESSFUL: utf-8')
	try: 
		open_codecs("utf-16")
	except: 
		print('UNSUCCESSFUL: utf-16')


