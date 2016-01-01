# encoder
convert data file to consistent encoding
if required, split into subfiles

Default parameters:

input file
name = 'input.csv'
delimiter = ','
quotechar = '"'

output file
delimiter = '\t'
quotechar = '"'

split_file = False
split_lines_per_file = 10000

Current encodings available:
* UTF-8
* UTF-16