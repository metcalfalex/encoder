
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
			for row in fi_csv:
				if fi_csv.line_num % (1/sample_percent)  == 0:
					fo_csv.writerow(row)
			print('SUCCESSFUL: '+str(encoding_name)+' codecs.open')


# -----------------------------------------------
# Parameters
# -----------------------------------------------

file_in = 'input_100.csv'
# file_in = './data/ansi.csv'
# file_in = './data/ascii.csv'
# file_in = './data/noheader.csv'
# file_in = './data/sample.csv'
# file_in = './data/utf-8.csv'
# file_in = './data/utf-16.csv'

delimiter_in = ','
quotechar_in = '"'

delimiter_out = '\t'
quotechar_out = '"'

sample_percent = 1
# e.g. 0.1 returns 10 percent of the full document (every 10th row)

file_out = 'output.txt'

# -----------------------------------------------
# Import
# -----------------------------------------------

# BASH
# sample first 100 lines for development
# head -100 input.csv > input_100.csv



# -----------------------------------------------
# Body
# -----------------------------------------------

try:
	open_codecs("utf-8")
except:
	print('UNSUCCESSFUL: utf-8 codecs.open')
	try: 
		open_codecs("utf-16")
	except: 
		print('UNSUCCESSFUL: utf-16 codecs.open')




# f = csv.reader(codecs.open(filepath, "r", encoding="utf-16"), delimiter=",", quotechar='"')

# try:    # checking if file exists
#     f = csv.reader(open(filepath, "r", encoding="cp1250"), delimiter=";", quotechar='"')
# except IOError:
#     f = []

# for record in f:
#     # do something with record
#     print(record)

# with open(file_out,'w') as fo:
# 	fo_csv = csv.writer(fo,delimiter=',')
# 	fo_csv.writerows(f)

# with open(file_out,'w') as fo:
# 	fo_csv = csv.writer(fo,delimiter=',')
# 	for record in f:
# 		fo.writerow(record)
# 		print(record)

# fo = open(file_out,'w')
# fo_csv = csv.writer(fo)
# for record in f:
# 	fo_csv.writerow(record)


	# fo_csv = csv.writer(fo,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)

# import codecs
# # import csv

# file_in = 'input_100.csv'
# file_out = 'output_100.txt'
# file_encoding = 'utf-16'

# fi = codecs.open(file_in, encoding = file_encoding)

# data = [line[:] for line in fi]

# with open(file_out,'w') as fo:
# 	fo.write(str(data))


# def open_codecs(file_in,file_encoding,file_out):
# 	with codecs.open(file_in, encoding = file_encoding) as fi:
# 		fi_csv = csv.reader(fi)
# 		data = [line[:] for line in fi]
# 		with codecs.open(file_out,'w','utf-8-sig') as fo:
# 			fo.write(data)
# 		with open(file_out,'w') as fo:
# 			fo.write(data)

# with open(file_out,'w') as fo:
# 	fo.write(str(data))
# with codecs.open(file_out,'w','utf-8-sig') as fo:
# 	fo.write(data)
# open_codecs(file_in,'utf-16',file_out)

# utf-8 | codecs.open
# utf-16 | codecs.open

# ascii | open rb
# ansi | open rb
# latin-1 | open rb
# utf-8 | open rb


# if inputenc == "utf-16" or inputenc == "utf-8":
# 	with codecs.open(file_in, encoding=inputenc) as fh:
# 		print [line[:] for line in fh]


# with open(file_in, 'rb') as fh:
# 	lines = [line[:] for line in fh]
# 	if inputenc == "ascii":
# 		lines = [line.decode("ascii") for line in lines]
# 	if inputenc == "ansi" or inputenc == "latin-1":
# 		lines = [line.decode("latin_1") for line in lines]
# 	if inputenc == "utf-8":
# 		lines = [line.decode("utf-8") for line in lines]

# 	stripped = []
# 	for line in lines:
# 		if line[-1] == '\n':
# 			if line[-2] == '\r':
# 				stripped.append(line[:-2])
# 			else:
# 				stripped.append(line[:-1])
# 		else:
# 			stripped.append(line)

# 	print stripped


# -----------------------------------------------
# Export
# -----------------------------------------------


