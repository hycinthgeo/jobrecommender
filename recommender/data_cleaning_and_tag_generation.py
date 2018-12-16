# -*- coding: utf-8 -*-
import os
import pandas as pd
import matplotlib.pyplot as plt

import helper_clean_data_google_skills as clean
import db_update as dbu

def main(csv_path, db_path):
	
	df = clean.read_and_drop_anomalies(csv_path)
	print "The input dataset has 7 columns: " + df.columns.values

	# (1) Creating cleaned tags for the raw fields; these tags will be used during job retrieval ----------------------	
	#(1a) Categorize locations
	df['tag_location'] = df['Location'].astype(str).apply(lambda x: clean.extract_location(x))
	#print df['tag_location']


	# (1b) Extract the career level tags		
	tags = clean.get_career_level_tags(df['Title'], mode = "tag mapping")
	df['career_level_tag'] = tags
	#vis.display_title_career_level(tags)


	# (1c) Extract minimum degree tag - if "Master/PhD", minimum degree = "Master"
	min_deg_level, pref_deg_level = clean.extract_degree_level_min_and_pref(df['Minimum Qualifications'], df['Preferred Qualifications'])
	df['min_degree_level'] = min_deg_level
	df['pref_degree_level'] = pref_deg_level
	#vis.display_education_pie_chart(df, 'min_degree_level', 'pref_degree_level')


	# (1d) Extract a list of all 'Category' - namely Google departments
	departments = sorted(list(set(df['Category'])))
	print "INFO: the listed %d jobs are from %d departments" %(len(df), len(departments))
	#vis.display_pie_chart(df, 'Category') 
	#plt.show()


	# (1e) Extracting education majors
	degree_tags = [[] for i in range(len(df))]
	degree_tags2 = [[] for i in range(len(df))]
	clean.extract_degree_ngram(df["Minimum Qualifications"], 1, degree_tags, "tag mapping") 
	clean.extract_degree_ngram(df["Preferred Qualifications"], 1, degree_tags2, "tag mapping") 
	df['min_degree_areas'] = degree_tags
	df['pref_degree_areas'] = degree_tags2
	#vis.display_major_tags(df, 'pref_degree_areas','Minimum Qualification: Education Majors')
	#vis.display_major_tags(df, 'pref_degree_areas','Preferred Qualification: Education Majors')

	# (1f) Extracting experience years
	min_years, pref_years = clean.extract_experience_years_min_and_pref(df['Minimum Qualifications'], df['Preferred Qualifications'])
	df['min_experience_years'] = min_years
	df['pref_experience_years'] = pref_years			
	#vis.display_pie_chart(df, 'min_experience_years','Minimum Qualification: Experience Years')
	#vis.display_pie_chart(df, 'pref_experience_years','Preferred Qualification: Experience Years') 

	# (1g) Extracting experience area
	tags_experience_area = [[] for i in range(len(df))]
	clean.extract_experience_area_ngram(df['Minimum Qualifications'], 2, tags_experience_area, mode = "tag mapping")
	df['min_experience_skills'] = tags_experience_area

	clean.extract_experience_area_ngram(df['Preferred Qualifications'], 2, tags_experience_area, mode = "tag mapping")
	df['pref_experience_skills'] = tags_experience_area

	# (2) Saving the pandas Dataframe as the 'job_listings' table in database----------------------	
	# (2a) connect to created db
	connection = dbu.__connect_db__(db_path);
	connection.text_factory = str
	cursor = connection.cursor()

	# (2b) create job listing table
	dbu.__create_job_listings_table_edited(1, db_path)


	# (2c) save new df to jobrecommendersystem.db
	for index, row in df.iterrows():
		# original info to display to the users
		Company = row['Company']
		Title = row['Title']
		Category = row['Category']
		Location = row["Location"]
		Minimum_Qualifications = row['Minimum Qualifications']
		Preferred_Qualifications = row['Preferred Qualifications']
		Responsibilities = row["Responsibilities"]

		# edited tag used for filtering and skill matching
		tag_title = row['career_level_tag'] 
		tag_loc = row['tag_location']
		tag_min_degree_type = row['min_degree_level']
		tag_min_degree_areas = " + ".join(strtag for strtag in row['min_degree_areas'])
		tag_min_exp_skills = " + ".join(strtag for strtag in row['min_experience_skills'])
		tag_min_exp_years = int(row['min_experience_years']) #-1 standard for "Unknown"

		tag_pref_degree_type = row['pref_degree_level']
		tag_pref_degree_areas = " + ".join(strtag for strtag in row['pref_degree_areas'])
		tag_pref_exp_skills = " + ".join(strtag for strtag in row['pref_experience_skills'])
		tag_pref_exp_years = int(row['pref_experience_years']) #-1 standard for "Unknown"

		#save to database		
		dbu.__insert_record_edited(cursor, Company, Title, Category, Location, Responsibilities, Minimum_Qualifications, Preferred_Qualifications, tag_title, tag_loc, tag_min_degree_type, tag_min_degree_areas, tag_min_exp_years, tag_min_exp_skills, tag_pref_degree_type, tag_pref_degree_areas, tag_pref_exp_years, tag_pref_exp_skills)

		connection.commit()
	
if __name__ == '__main__':
	Jupyter_notebook_system = "Linux"

	if Jupyter_notebook_system == "Windows":
		sys_path = os.getcwd() + "\..\database\\"
	else:
		sys_path = os.getcwd() + "/../database/"
	print sys_path

	csv_path = sys_path + "job_skills.csv"
	db_path = sys_path + "jobrecommendersystem.db"

	main(csv_path, db_path)


	
	


