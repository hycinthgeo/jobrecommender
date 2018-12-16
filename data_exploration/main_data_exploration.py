# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import os
import helper_clean_data_google_skills as clean
import operator
import re
import string


if __name__ == '__main__':
	
	sys_path = os.getcwd()
	csv_path = sys_path + "/../database/job_skills.csv"
	#df = pd.read_csv (csv_path,sep = ',')
	#df = df.drop(index = 100) #corner case - Job list in Japanese
	df = clean.read_and_drop_anomalies(csv_path)

	# Understand the key frequent words per career category	
	key_word = "Intern"
	N_gram = 2
	filter_on = True #turn on the filter to show only when the N_gram ended with key_word
	print_ngram = True
	print_warning_log = True #check to ensure your are satisfied with the tagging rule
	tags = [None for i in range(len(df))]
	count = clean.extract_title_ngram(df['Title'], "Intern", N_gram, tags, filter_on, print_ngram, print_warning_log) 

	# In this example, data exploration results suggested that 
	#"Legal Intern", "Engineer Intern", , "Industrial Design Intern", , "User Experience Design Intern", "User Experience Writer Intern", "User Experience Research Intern", "User Experience Engineer Intern"


	# Understand the key frequent words in degree
	tags = clean.get_career_level_tags(df['Title'], mode = "data exploration")
	# Based on this results, we merged some positions, and saved it as a map in helper_mapping_dictionaries.py

	# Explore the education majors; clean each "career level" once upon a time
	tags = clean.get_career_level_tags(df['Title'], mode = "tag mapping")
	df['career_level_tag'] = tags
	print sorted((list(set(df['career_level_tag']))))
	filter1 = df['career_level_tag'] == "Analyst"
	filtered_df = df[filter1].reset_index()
	print len(filtered_df)

	degree_tags = [[] for i in range(len(filtered_df))]
	clean.extract_degree_ngram(filtered_df["Minimum Qualifications"], 2, degree_tags, "data exploration") #Ngram 1-3

	#	
	df = df[df['career_level_tag'] == "Manager/Advisor/Lead"] 
	print len(df)
	tags_experience_area = [[] for i in range(len(df))]
	clean.extract_experience_area_ngram(df['Minimum Qualifications'],2, tags_experience_area, mode = "data exploration")

	#skills
	

	

	#Trainer/Teacher, HR, doesn't have much education degree specification

#legal- no degree requirement?
