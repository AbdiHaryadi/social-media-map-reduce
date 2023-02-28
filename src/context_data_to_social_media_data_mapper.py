#!/home/bigdata/anaconda3/bin/python

import sys

context_social_media_map = {
	"facebook_post": "facebook",
	"instagram_comment": "instagram",
	"instagram_graph_data": "instagram",
	"instagram_post": "instagram",
	"instagram_status": "instagram",
	"twitter_status": "twitter",
	"youtube_comment": "youtube",
	"youtube_video": "youtube"
}

for line in sys.stdin: # Inputting filepath
	data = line.strip().split("\t")
	if  len(data) != 3:
		continue # Skip

	context, _, date = data
	social_media = context_social_media_map[context]
	count = 1

	print(social_media, date, count, sep=",")

