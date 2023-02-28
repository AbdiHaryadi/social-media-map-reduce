#!/home/bigdata/anaconda3/bin/python

import sys

current_context = None
current_entity_id = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if  len(data) != 3:
		continue # Skip

	context, entity_id, date = data

	if context == current_context and entity_id == current_entity_id:
		continue # Skip duplicate entity

	print(context, entity_id, date, sep="\t")
	current_context = context
	current_entity_id = entity_id

