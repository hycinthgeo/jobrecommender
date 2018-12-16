# -*- coding: utf-8 -*-
Jupyter_notebook_system = "Linux"  # affect directory path

import pandas as pd
from recommender import db_update as dbu # SQL updating modul
from recommender import data_cleaning_and_tag_generation as tag # Data cleaning and tagging
from recommender import interactive_retrieval as rt # Recommender system - computation module
from recommender import interactive_retrieval_vis as rtv # Recommender system - visualziation module
import os
#import matplotlib.pyplot as plt
#import helper_mapping_dictionaries as mmp


def main():
	# file path for the original csv file and the final database to save cleaned features 
	sys_path = os.getcwd()
	if Jupyter_notebook_system == "Windows":
		csv_path = sys_path + "\database\job_skills.csv"
		db_path = sys_path + "\database\jobrecommendersystem.db"
		fig_dir_path = sys_path + "\figs" 
	else:
		csv_path = sys_path + "/database/job_skills.csv"
		db_path = sys_path + "/database/jobrecommendersystem.db"
		fig_dir_path = sys_path + "/figs/" 		

	
		"""
		csv_path = os.getcwd() + "\database\job_skills.csv"
		db_path = os.getcwd() + "\database\jobrecommendersystem.db"
	else:
		csv_path = os.getcwd() + "/database/job_skills.csv"
		db_path = os.getcwd() + "/database/jobrecommendersystem.db"
	"""

	print "Input CSV file location:              " + csv_path
	print "Cleaned and tagged database location: " + db_path
	print "Output figure locations: 			 " + fig_dir_path

	#Section 1: Optional, create the database --------------------------------------------------------------------------------
	#print "Step 1: Creating job listing table and save to the database"
	# getting published data cleaned and feature extracted - re-create the database if enabled
	tag.main(csv_path, db_path)


	#Section 2: optional, visaulize the dataframe of all data update the database----------------------------------------------
	#df_all = dbu.__fetch_results_from_db_edited(db_path, "all")
	#df_loc_count = rt.retrive_location_counter(df_all)
	#df_loc_count = rt.attribute_counter(df_all['Location'], 'Location')
	#print df_all.columns.values
	#df_all.head(5)


	#Section 3----------------------Filter jobs based on position category and working years------------------------------------- 
	df_min, df_pref = rt.first_round_user_info_by_qa(db_path)

	rtv.first_round_user_query_visualization(df_min, 'min',fig_dir_path)
	rtv.first_round_user_query_visualization(df_pref, 'pref',fig_dir_path)

	#Section 4---------------------second round user input: degree, major, interested/uninterested skill--------------------------
	df, match_level, my_highest_edu, my_majors, my_skills, my_un_skills, my_responsibilities = rt.second_round_user_info_by_qa(df_min, df_pref)

	# compute scores
	unlike_penalty = 1
	df_w_scores = rt.get_featured_scores(df, match_level, my_highest_edu, my_majors, my_skills, my_un_skills, unlike_penalty, my_responsibilities)
	#print df_w_scores[['Title','degree_matched','scaled_major_score','scaled_skill_score','scaled_resp_sim']].head()

	# compute final score
	df_top10 = rt.compute_final_score_return_top10(df_w_scores, 1.0/3, 1.0/3, 1.0/3)

	# plot for review
	print df_top10[['final_score', 'Title','Location']]
	rtv.plot_3D_results(df_top10['scaled_resp_sim'], df_top10['scaled_skill_score'], df_top10['scaled_major_score'], df_top10.index, df_top10['Title'], df_top10['tag_loc'], fig_dir_path)   


#-----------------------------Final lookup------------------------------------ 
	rt.lookup_a_recommended_job(df_top10)    

if __name__ == '__main__':
    main()












