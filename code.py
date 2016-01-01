
# -----------------------------------------------
# Resources
# -----------------------------------------------


# -----------------------------------------------
# Libraries
# -----------------------------------------------

import csv
import codecs
import math

# -----------------------------------------------
# Functions
# -----------------------------------------------


def open_codecs(encoding_name):
	# attempt to open input file
	with codecs.open(file_in, "r", encoding=encoding_name) as fi:
		fi_csv = csv.reader(fi, delimiter=delimiter_in, quotechar=quotechar_in)
		# store header incase split files are desired
		header_line = next(fi_csv)
		if split_file == False:
			with open('output.txt','w') as fo:
				fo_csv = csv.writer(fo,delimiter=delimiter_out, quotechar=quotechar_out)
				fo_csv.writerow(header_line)
				for row in fi_csv:
					fo_csv.writerow(row)
				print('SUCCESSFUL: '+str(encoding_name)+' codecs.open')
		else:
			# count lines
			with codecs.open(file_in, "r", encoding=encoding_name) as fi_count:
				for i, l in enumerate(fi_count):
					pass
				total_lines = i + 1
			# calculate number of files required
			n_files_required = math.floor((total_lines - 1) / split_lines_per_file)+1
			# loop through files
			for f in range(n_files_required):
				with open('output_'+str(f+1).zfill(3)+'.txt','w') as fo:
					fo_csv = csv.writer(fo,delimiter=delimiter_out, quotechar=quotechar_out)
					fo_csv.writerow(header_line)
					for row in fi_csv:
						fo_csv.writerow(row)
						if fi_csv.line_num % split_lines_per_file == 0:
							break
			print('SUCCESSFUL: '+str(encoding_name)+' codecs.open')


# -----------------------------------------------
# Parameters
# -----------------------------------------------

file_in = 'input.csv'
delimiter_in = ','
quotechar_in = '"'

delimiter_out = '\t'
quotechar_out = '"'

split_file = False
split_lines_per_file = 10000


# -----------------------------------------------
# Body
# -----------------------------------------------

try:
	open_codecs("utf-8")
except Exception as e:
	print('UNSUCCESSFUL: utf-8\n'+str(e))
	try: 
		open_codecs("utf-16")
	except Exception as e:
		print('UNSUCCESSFUL: utf-16\n'+str(e))


