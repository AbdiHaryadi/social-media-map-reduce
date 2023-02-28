#!/home/bigdata/anaconda3/bin/python

import sys

for line in sys.stdin: # Inputting filepath
	filepath = line.strip()
	if filepath != "":
		with open(filepath, mode="r") as file:
			data = file.read()

		print(filepath, data.replace("\t", " ").replace("\n", " "), sep="\t")





























