import sqlite3
import pandas as pd

# Connect to SQL database
def __connect_db__(final_path):
	"""Connect to the specific database."""
	connection = sqlite3.connect(final_path)
	connection.row_factory = sqlite3.Row
	return connection

# Drop a table if already existing in db
def __drop_table(cursor):
    cursor.execute('DROP TABLE IF EXISTS job_listings')

# Create "job_listings" table
def __create_job_listings_table_edited(create, final_path):
    if create:
        connection = __connect_db__(final_path);
        cursor = connection.cursor();
        __drop_table(cursor)
        cursor.execute('CREATE TABLE job_listings(Company TEXT, Title TEXT, Category TEXT, Location TEXT, Responsibilities TEXT, Minimum_Qualifications TEXT, Preferred_Qualifications TEXT, tag_title TEXT, tag_loc TEXT, tag_min_degree_type TEXT, tag_min_degree_areas TEXT, tag_min_exp_years INT, tag_min_exp_skills TEXT, tag_pref_degree_type TEXT, tag_pref_degree_areas TEXT, tag_pref_exp_years INT, tag_pref_exp_skills TEXT)')
        cursor.close()
        connection.close()

# Insert record into "job_listings" table
def __insert_record_edited(cursor, Company, Title, Category, Location, Responsibilities, Minimum_Qualifications, Preferred_Qualifications, tag_title, tag_loc, tag_min_degree_type, tag_min_degree_areas, tag_min_exp_years, tag_min_exp_skills, tag_pref_degree_type, tag_pref_degree_areas, tag_pref_exp_years, tag_pref_exp_skills):	
	cursor.execute(
	'INSERT OR REPLACE INTO job_listings (Company, Title, Category, Location, Responsibilities, Minimum_Qualifications, Preferred_Qualifications, tag_title, tag_loc,  tag_min_degree_type, tag_min_degree_areas, tag_min_exp_years, tag_min_exp_skills, tag_pref_degree_type, tag_pref_degree_areas, tag_pref_exp_years, tag_pref_exp_skills) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (Company, Title, Category, Location, Responsibilities, Minimum_Qualifications, Preferred_Qualifications, tag_title, tag_loc, tag_min_degree_type, tag_min_degree_areas, tag_min_exp_years, tag_min_exp_skills, tag_pref_degree_type, tag_pref_degree_areas, tag_pref_exp_years, tag_pref_exp_skills))

# Fetch jobs based on the query_title, return as a pandas Dataframe
def __fetch_results_from_db_edited(db_path, query_title):
	
	conn = sqlite3.connect(db_path)
	if query_title == "all":
		df = pd.read_sql_query("select * from job_listings", conn)
	else:
		df = pd.read_sql_query("select * from job_listings where tag_title = %s;" %("'" + query_title + "'"), conn)
	conn.close()
	return df

