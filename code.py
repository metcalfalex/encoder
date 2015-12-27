
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




# -----------------------------------------------
# Parameters
# -----------------------------------------------


filepath = 'input_100.csv'
file_out = 'output.csv'

# -----------------------------------------------
# Import
# -----------------------------------------------

# BASH
# sample first 100 lines for development
# head -100 input.csv > input_100.csv



# -----------------------------------------------
# Body
# -----------------------------------------------



with codecs.open(filepath, "r", encoding="utf-16") as fi:
	fi_csv = csv.reader(fi, delimiter=",", quotechar='"')
	with open(file_out,'w') as fo:
		fo_csv = csv.writer(fo,delimiter=',')
		fo_csv.writerows(fi_csv)


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


