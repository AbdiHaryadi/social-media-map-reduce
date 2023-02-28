#!/home/bigdata/anaconda3/bin/python

import sys

current_social_media = None
current_date = None
current_count = 0
for line in sys.stdin: # Inputting filepath
	data = line.strip().split(",")
	if  len(data) != 3:
		continue # Skip

	social_media, date, count = data
	count = int(count)

	if current_social_media is None:
		current_social_media = social_media
		current_date = date
		current_count = count
	elif social_media == current_social_media and date == current_date:
		current_count += count
	else:
		print(current_social_media, current_date, current_count, sep=",")
		current_social_media = social_media
		current_date = date
		current_count = count

if current_social_media is not None:
	print(current_social_media, current_date, current_count, sep=",")
