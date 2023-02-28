#!/home/bigdata/anaconda3/bin/python

import sys
import random

random.seed(1234)

for line in sys.stdin: # Inputting filepath
	filepath = line.strip()
	if filepath != "" and random.random() < 0.1:
		with open(filepath, mode="r") as file:
			data = file.read()

		print(filepath, data.replace("\t", " ").replace("\n", " "), sep="\t")





























