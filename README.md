# MapReduce Scripts for Social Media Data

All scripts used is in `src`.

## How to Use It
Before I tell how to use it, note that even this repository is public, the folder of social media data `raw_json` is still private.
The reason is there are no publicable statement for this data. So, yeah, I am sorry if you can't use it.
I make this public so the examiners can access my work.

1. Get all local filepath for each file in `raw_json`. You can use `os.listdir` for this. Save it to one file, let's say `filelist.txt`.
2. Go to project root directory. Execute `cat ./filelist.txt | ./src/filepaths_to_single_file.py > data.txt`. If your machine can't handle too-big data, just like mine, use `10_percents_filepaths_to_single_file.py` instead.
3. Do `hdfs dfs -mkdir /social_media`.
4. Do `hdfs dfs -copyFromLocal path/to/project/data.txt /social_media/data.txt`.
5. Do `hadoop jar /path/to/hadoop/hadoop-3.2.2/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar -input /social_media/10_percents_data.txt -mapper path/to/project/src/context_data_extractor_mapper.py -reducer path/to/project/src/remove_duplicated_context_data_reducer.py -output /social_media/intermediate_result`. You may want to adjust all paths used in this command.
6. Do `hadoop jar /path/to/hadoop/hadoop-3.2.2/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar -input /social_media/intermediate_result/part-00000 -mapper path/to/project/src/context_data_to_social_media_data_mapper.py -reducer path/to/project/src/social_media_data_reducer.py -output /social_media/final_result`. You may want to adjust all paths used in this command.
7. Do `hdfs dfs -copyToLocal /social_media/final_result/part-00000 path/to/project/result.csv`.

## About
This repository was created by M. Abdi Haryadi. H (13519156) for Task I IF4044 Big Data Technology 2022-2.

