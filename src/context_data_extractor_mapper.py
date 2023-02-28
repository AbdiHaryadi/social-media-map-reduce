#!/home/bigdata/anaconda3/bin/python

from datetime import datetime
import json
import re
import subprocess
import sys

facebook_post_filepath_matcher = re.compile(r".*facebook_post_[0-9]+_.+\.json")
instagram_comment_filepath_matcher = re.compile(r".*instagram_comment_[0-9]+_.+\.json")
instagram_post_filepath_matcher = re.compile(r".*instagram_post_[0-9]+_.+\.json")
instagram_status_filepath_matcher = re.compile(r".*instagram_status_[0-9]+\.json")
instagram_user_filepath_matcher = re.compile(r".+.json.json")
twitter_status_filepath_matcher = re.compile(r".*twitter_status_[0-9]+_.+\.json")
youtube_comment_filepath_matcher = re.compile(r".*youtube_comment_[0-9]+_.+\.json")
youtube_video_filepath_matcher = re.compile(r".*youtube_video_[0-9]+_.+\.json")


def handle_facebook_post(content):
	post_list = json.loads(content)

	for post in post_list:
		post_id = post["id"]
		post_datetime_string = post["created_time"]  # Example value: 2022-01-12T05:19:28+0000
		post_datetime = datetime.fromisoformat(post_datetime_string.replace("+0000", "+00:00"))
		post_date_string = post_datetime.strftime("%Y-%m-%d")

		print("facebook_post", post_id, post_date_string, sep="\t")

def instagram_timestamp_string_to_date_string(timestamp_string):
	 # Example timestamp string: 1634883366
	return datetime.fromtimestamp(int(timestamp_string)).strftime("%Y-%m-%d")

def handle_instagram_comment(content):
	comment_list = json.loads(content)

	for comment in comment_list:
		comment_id = comment["id"]
		comment_timestamp_string = comment["created_time"]
		comment_date_string = instagram_timestamp_string_to_date_string(comment_timestamp_string)

		print("instagram_comment", comment_id, comment_date_string, sep="\t")

def handle_instagram_post(content):
	post_list = json.loads(content)

	for post in post_list:
		post_id = post["id"]
		post_timestamp_string = post["created_time"]
		post_date_string = instagram_timestamp_string_to_date_string(post_timestamp_string)

		print("instagram_post", post_id, post_date_string, sep="\t")

def handle_instagram_status(content):
	status_list = json.loads(content)

	for status in status_list:
		status_id = status["id"]
		status_timestamp_string = status["created_time"]
		status_date_string = instagram_timestamp_string_to_date_string(status_timestamp_string)

		print("instagram_status", status_id, status_date_string, sep="\t")

def handle_instagram_user(content):
	raw_data = content

	try:
		json_data = json.loads("{" + raw_data)
		can_be_parsed = True

	except json.decoder.JSONDecodeError:
		can_be_parsed = False

	if can_be_parsed:
		graph_data_list = json_data["GraphImages"]
		for graph_data in graph_data_list:
			graph_data_id = graph_data["id"]
			graph_data_timestamp_string = graph_data["taken_at_timestamp"]
			graph_data_date_string = instagram_timestamp_string_to_date_string(graph_data_timestamp_string)
			print("instagram_graph_data", graph_data_id, graph_data_date_string, sep="\t")

			for comment in graph_data["comments"]["data"]:
				comment_id = comment["id"]
				comment_timestamp_string = comment["created_at"]
				comment_date_string = instagram_timestamp_string_to_date_string(comment_timestamp_string)

				print("instagram_comment", comment_id, comment_date_string, sep="\t")
			
		

def handle_twitter_status(content):
	status_list = json.loads(content)

	for status in status_list:
		status_id = status["id"]
		status_datetime_string = status["created_at"]
		status_datetime_format = "%a %b %d %H:%M:%S %z %Y" # Example value: Fri Jan 01 05:03:05 +0000 2021
		status_datetime = datetime.strptime(
			status_datetime_string,
			status_datetime_format
			
		)
		status_date_string = status_datetime.strftime("%Y-%m-%d")

		print("twitter_status", status_id, status_date_string, sep="\t")

def handle_youtube_comment(content):
	comment_list = json.loads(content)

	for comment in comment_list:
		if comment["kind"] == "youtube#comment":
			comment_id = comment["id"]
			comment_datetime_string = comment["snippet"]["publishedAt"] # Example value: 2022-01-24T12:55:18Z
			comment_datetime = datetime.fromisoformat(comment_datetime_string.replace("Z", "+00:00"))
			comment_date_string = comment_datetime.strftime("%Y-%m-%d")

			print("youtube_comment", comment_id, comment_date_string, sep="\t")

def handle_youtube_video(content):
	video_list = json.loads(content)

	for video in video_list:
		if video["kind"] == "youtube#video":
			video_id = video["id"]
			video_datetime_string = video["snippet"]["publishedAt"] # Example value: 2022-01-24T12:55:18Z
			video_datetime = datetime.fromisoformat(video_datetime_string.replace("Z", "+00:00"))
			video_date_string = video_datetime.strftime("%Y-%m-%d")

			print("youtube_video", video_id, video_date_string, sep="\t")
	
for line in sys.stdin: # Inputting filepath
	filepath, content = line.strip().split("\t")

	if facebook_post_filepath_matcher.match(filepath):
		handle_facebook_post(content)
	elif instagram_comment_filepath_matcher.match(filepath):
		handle_instagram_comment(content)
	elif instagram_post_filepath_matcher.match(filepath):
		handle_instagram_post(content)
	elif instagram_status_filepath_matcher.match(filepath):
		handle_instagram_status(content)
	elif instagram_user_filepath_matcher.match(filepath):
		handle_instagram_user(content)
	elif twitter_status_filepath_matcher.match(filepath):
		handle_twitter_status(content)
	elif youtube_comment_filepath_matcher.match(filepath):
		handle_youtube_comment(content)
	elif youtube_video_filepath_matcher.match(filepath):
		handle_youtube_video(content)

	# else: ignore it

		
		

