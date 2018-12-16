import pandas as pd
import matplotlib.pyplot as plt

import helper_mapping_dictionaries as mmp
import db_update as dbu
import helper_cosine_sim_calculator as sim_cosine


def fetch_all_pos(my_poses, my_years, mode, db_path):
    df = dbu.__fetch_results_from_db_edited(db_path, my_poses[0])
    
    for i in range(1, len(my_poses)):
        df_cur = dbu.__fetch_results_from_db_edited(db_path, my_poses[i])
        #df = [df, df_cur]
        df = df.append(df_cur, ignore_index=True)
    #print (len(df))
    # filter_year
    df = df[df['tag_' + mode + '_exp_years'] <= my_years]
    df = df.reset_index().drop(['index'], axis = 1)

    return df


def attribute_counter(array, attribute_name):

    array_count = dict()
    for i in array:
        if i != "" and i!= " ":
            array_count.setdefault(i, 0)
            array_count[i] += 1

    df_array_count = pd.DataFrame.from_dict(sorted(array_count.iteritems()))
    df_array_count.columns = [attribute_name, 'Count']
    return df_array_count

def long_attribute_counter(array, attribute_name):

    array_count = dict()
    for i in array:
        if i != "" and i!= " ":
            
            for j in i.split(" + "):
                array_count.setdefault(j.strip(), 0)
                if len(j) > 0:
                	array_count[j.strip()] += 1

    df_array_count = pd.DataFrame.from_dict(sorted(array_count.iteritems()))
    df_array_count.columns = [attribute_name, 'Count']
    df_array_count['Percent'] = 100.0 * df_array_count['Count']/len(array)
    return df_array_count
		

def get_jobs_from_locations(my_places, df_in):
    valid = [0 for i in range(len(df_in))]
    for my_place in my_places:
        for j in range(len(df_in)):
            if my_place == df_in.iloc[j]['tag_loc']:
                valid[j] = 1
    df_in['valid'] = pd.Series(valid)
    df_out = df_in[df_in['valid'] == 1]
    df_out.reset_index()
    df_out = df_out.drop(['valid'], axis = 1)
    return df_out


def first_round_user_info_by_qa(db_path):
	#connect to db
	
    print "INFO: The firstr-round query aims at collecting the user's basic preferences, including\n"\
            "    (1) interested position\n    (2) your experience years\n    (3) interested locations\n"

    print "INFO1: Here are all available positions"
    print "%10s %40s" %("Index", "Position")
    career_level_maps = mmp.career_level_maps
    i = 0
    list_pos = []
    for k, v in career_level_maps.iteritems():
        print "%10s %40s" %(str(i), k)
        list_pos.append(k)
        i += 1    

    # Positions
    my_poses = raw_input("QUESTION 1: What are your interested positions\n    Hints: Put the Index\n    Example: 0, 7\n")
    my_poses = my_poses.split(",")
    my_poses = [list_pos[int(my_poses[i].strip())] for i in range(len(my_poses))]
    str_my_poses = my_poses[0]
    for i in range(1, len(my_poses)):
        str_my_poses += (", " + my_poses[i])
    print "INFO1: Your chosen titles include " + str_my_poses

    # Experience
    print
    my_years = raw_input("QUESTION 2: How long have your been working (years)?\n    Example: 5.5\n")
    my_years = int(my_years)
    print "INFO2: You have %2s years of working experience " %(str(my_years))

    df_min = fetch_all_pos(my_poses, my_years, 'min', db_path)
    df_pref = fetch_all_pos(my_poses, my_years, 'pref', db_path)

    print
    print "INFO3: Your interested jobs are available in the following locations\n"
    df_loc_count = attribute_counter(df_min['tag_loc'], 'tag_loc')
    list_loc = []
    for i in range(len(df_loc_count)):
        list_loc.append(df_loc_count.iloc[i]['tag_loc'])

    print df_loc_count
    print len(list_loc)
    my_places = raw_input("QUESTION 3: Where would you like to work?\n   Hint: Put the Index\n    Example: 22, 24, 26\n ")

    my_places = my_places.split(",")
    #print my_places
    my_places = [list_loc[int(my_places[i].strip())] for i in range(len(my_places))]
    #print my_places


    df_min = get_jobs_from_locations(my_places, df_min)   
    df_loc_count = attribute_counter(df_min['tag_loc'], 'tag_loc')
    print
    print "INFO: %5d jobs found: you meet minimum qualifcations based on title/working experience/locations" %(len(df_min))
    print df_loc_count
    print "INFO: Jobs that you are satisfying the Preferred qualifcations based on title/working experience/locations"
    df_pref = get_jobs_from_locations(my_places, df_pref) 
    df_loc_count = attribute_counter(df_pref['tag_loc'], 'tag_loc')
    print
    print "INFO: %5d jobs found: you meet minimum qualifcations based on title/working experience/locations" %(len(df_pref))
    print df_loc_count
    
          
    return df_min, df_pref
    


def second_round_user_info_by_qa(df_min, df_pref):
    print 
    # Get the matching level ------------------------------------------------------------------------------
    print "INFO: Please let the job recommender system knows more about you\n"
    match_level = raw_input("QUESTION 1: Would you like to match minimum or preferred qualifications?\n	Hints: type min or pref\n")
    print "\nINFO: you have chosen to match = %5s Qualifications" %(match_level)
    if match_level == "min":
        df = df_min
    else:
        df = df_pref

    df.reset_index()

    # Get the user's highest education--------------------------------------------------------------------
    print "INFO: your interested jobs accept the following minimum educations\n"
    edu_level = sorted(list(set(df['tag_' + match_level + '_degree_type'])))
    for i in range(len(edu_level)):
        print i, edu_level[i]
    my_highest_edu = raw_input("QUESTION:2 What's your highest education? \n"\
                                "Hint: put leftmost index for majors\n"\
                                "Example: N/A, Bachelor, Master, MBA only, PhD\n")
    #my_highest_edu = edu_level[int(my_highest_edu)]
    print "INFO: your highest education is %s" %(my_highest_edu)  
    
    
    # Get the user's degree majors------------------------------------------------------------------------
    print "INFO: your interested jobs accept the following majors\n"
    majors = sorted(list(set(df['tag_' + match_level + '_degree_areas'])))
    major_list = set()
    #print majors
    for i in range(len(majors)):
        temp = majors[i].split("+")
        for j in temp:
            if j.strip() not in major_list and j.strip() != u'':
                major_list.add(j.strip())

    major_list = list(major_list)
    for i in range(len(major_list)):
        print i, major_list[i]
    my_majors = raw_input("QUESTION:2 What's your degree majors? \n"\
                                "Hint: put leftmost index for majors\n"\
                                "Example: 1, 2\n")
    my_majors_int = my_majors.split(",")
    my_majors = []
    for major_ind in my_majors_int:
        my_majors.append(major_list[int(major_ind)])
        
    str_my_majors = major_list[int(my_majors_int[0])]
    for i in range(1, len(my_majors_int)):
        str_my_majors += (", " + major_list[int(my_majors_int[i])])
    print "INFO: your studied majors include %s" %(str_my_majors)  
    
    # Get the user's interested and uninterested skills
    print "INFO: your interested jobs likes the following skills\n"

    def get_lists(array):
        skills = sorted(list(set(array)))

        skill_list = set()
        #print skills
        for i in range(len(skills)):
            temp = skills[i].split("+")
            for j in temp:
                if j.strip() not in skill_list and j.strip() != u'':
                    skill_list.add(j.strip())

        skill_list = list(skill_list)
        for i in range(len(skill_list)):
            print i, skill_list[i]


        my_skills = raw_input("QUESTION:3a What are your interested matching experience/skills? \n"\
                                    "Hint: put leftmost index for skills\n"\
                                    "Example: 1, 2\n")
        my_skills = my_skills.split(",")
        my_skills = [skill_list[int(my_skill)] for my_skill in my_skills ]

        my_un_skills = raw_input("QUESTION:3b What are your uninterested matching experience/skills? \n"\
                                    "Hint: put leftmost index for skills\n"\
                                    "Example: 1, 2\n")
        my_un_skills = my_un_skills.split(",")
        my_un_skills = [skill_list[int(my_un_skill)] for my_un_skill in my_un_skills ]


        return skill_list, my_skills, my_un_skills

    skill_list, my_skills, my_un_skills = get_lists(df['tag_' + match_level + '_exp_skills'])
    str_my_skills, str_my_un_skills = my_skills[0], my_un_skills[0]

    for i in range(len(my_skills)):
        str_my_skills += (", ") + my_skills[i]

    for i in range(len(my_un_skills)):
        str_my_un_skills += (", ") + my_un_skills[i]    

    print "INFO: your matching skills include %s" %(str_my_skills)  
    print "INFO: your uninterested matching skills include %s" %(str_my_un_skills) 
    
    # Get the user's responsibilities ------------------------------------------------------------------------
    my_responsibilities = raw_input("QUESTION:4 What are your responsibilities in previous jobs? \n"\
                            "	Hint: put any descriptions in English, consider copying from your resume\n"\
                            "	Example: Design, develop, test, deploy, maintain and improve software."\
							"Manage individual project priorities, deadlines and deliverables.\n")

    return df, match_level, my_highest_edu, my_majors, my_skills, my_un_skills, my_responsibilities




def lookup_a_recommended_job(df_top10):
	index = None


	while index != "stop":
		index = raw_input("QUESTION: Which position would you like to know more details?\n	Example: 1\n	Example: 'stop' to terminate inquiry\n")
		if index == "stop":
			return 
		post = df_top10.iloc[int(index)]
		print 
		print "Basic Job Info -----------------------------------------------------------------------------------------"
		print "%45s | %20s | %20s" %("Title", "Department", "Location")
		print "%45s | %20s | %20s" %(post["Title"], post["Category"], post["Location"])
	
		print		
		print "Minimum Qualfications ------------------------------------------------------------------------------------"
		print post["Minimum_Qualifications"]

		print
		print "Preferred Qualfications -----------------------------------------------------------------------------------"
		print post["Preferred_Qualifications"]	

		print
		print "Responsibilities-------------------------------------------------------------------------------------------"
		print post["Responsibilities"]    

	return 



def compare_degree(my_degree, degree):
    degree_rank = ["N/A", "Bachelor", "Master", "MBA&Master", "MBA only", "PhD", "JD"]
    if degree_rank.index(my_degree) >= degree_rank.index(degree):
        return 1
    else:
        return 0
    
    
def count_normalized_skills(my_skills, ref_skills):
    count = 0
    for my_skill in my_skills:
        if my_skill in ref_skills:
            count += 1
    return 1.0 * count/len(ref_skills)

def MinMaxScalar(array):
    op = [0 for i in range(len(array))]
    if len(array) <= 1:
		return array
    for i in range(len(array)):
        op[i] = 1.0 * (array[i] - min(array))/(max(array) - min(array))
    return op
        

def get_featured_scores(df, match_level, my_highest_edu, my_majors, my_skills, my_un_skills, unlike_penalty, my_responsibilities):
    
    df = df.reset_index()
    degree_matched = []
    scaled_major_score = []
    scaled_skill_score = []
    scaled_resp_sim = []
    
    
    for i in range(len(df)):
        post = df.iloc[i]
        
        #match degree
        ref_degree = post['tag_' + match_level + '_degree_type']
        if compare_degree(my_highest_edu, ref_degree):
            degree_matched.append(1)
        else:
            degree_matched.append(0)
            
        # major scoring, linear
        ref_majors = post['tag_'+match_level+'_degree_areas'].split(" + ")
        if ref_majors == ["N/A"]:
            my_max = 0.5
            
        N = len(ref_majors)
        
        my_max = 0
        #print my_majors, ref_majors
        for my_major in my_majors:
            
            for j in range(len(ref_majors)):
                
                if my_major in ref_majors[j]:
                    score = (N - j)*1.0/N
                    if score > my_max:
                        my_max = score     
                #print score, N, j
        
        scaled_major_score.append(my_max)     
        
        # skills, and penalty for disliked skills
        ref_skills = post['tag_'+match_level+'_exp_skills'].split(" + ")
        count_skills = count_normalized_skills(my_skills, ref_skills)
        count_unskills = count_normalized_skills(my_un_skills, ref_skills)
        dif = count_skills - unlike_penalty * count_unskills 
        scaled_skill_score.append(dif)
        
        # Cosine similarity score
        ref_resp = post['Responsibilities']
        scaled_resp_sim.append(sim_cosine.get_sim(my_responsibilities, ref_resp))
        
        
    # MinMaxScalar to 0 ~ 1
    
    
        
    df['degree_matched'] = pd.Series(degree_matched)
    df['scaled_major_score'] = pd.Series(MinMaxScalar(scaled_major_score))
    df['scaled_skill_score'] = pd.Series(MinMaxScalar(scaled_skill_score))
    df['scaled_resp_sim'] = pd.Series(MinMaxScalar(scaled_resp_sim))
    
    return df

def compute_final_score_return_top10(df_w_scores, w1, w2, w3):
    final_score = [0 for i in range(len(df_w_scores))]
    for i in range(len(final_score)):
        final_score[i] = df_w_scores['scaled_resp_sim'][i] * w1 + df_w_scores['scaled_skill_score'][i] * w2 + df_w_scores['scaled_major_score'][i] * w3;

    df_w_scores["final_score"] = pd.Series(final_score)
    #sorted descending
    df_w_scores.sort_values(by = "final_score", ascending= False, inplace = True)
    df_w_scores.reset_index(inplace = True)
    df_top_10 = df_w_scores[:10]
    return df_top_10

















	
