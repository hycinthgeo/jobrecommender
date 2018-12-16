# -*- coding: utf-8 -*-


from nltk import FreqDist
from nltk.util import ngrams   
import string
import helper_mapping_dictionaries as mmp
import pandas as pd

# (1) extract minimum degree requirement 
# (2) tag career level (mode = data exploration, extract N-gram and popular phrases; mode = tag mapping, tag career level)
# (3) tag education degree (mode = data exploration, extract N-gram and popular phrases; mode = tag mapping, tag career level)
# Helper function: computer_freq


def read_and_drop_anomalies(csv_path):
	df = pd.read_csv (csv_path,sep = ',')
	valid = []
	for i in range(len(df)):
		min_qual = df.iloc[i]['Minimum Qualifications']
		if type(min_qual) == float or min_qual == "nan" or min_qual is None or i == 100: #index = 100 - Japanese
		    valid.append(False)
		else:
		    valid.append(True)
	df['valid'] = pd.Series(valid)
	df = df[df['valid'] == True]
	df.drop(['valid'], axis=1, inplace=True)
	df.reset_index(drop=True, inplace=True)
	#print df
	return df



def extract_location(loc):
	loc = loc.split(",")
	#print loc[-1]
	if "United States" in loc[-1]:
	    city = loc[0]
	    state = loc[1]
	    loc = "USA: " + city + ", " + state
	else:
	    loc = loc[-1] #country
	return loc

	

def extract_min_degree(min_qual):
	#print min_qual
	#print min_qual
	#min_qual = min_qual.encode("utf-8")
	degrees = []
	min_degree = "N/A"
	accept_prac_experience = "N/A"
	
	if type(min_qual) == float or min_qual == "nan" or min_qual is None:
		min_degree = "N/A"
		return min_degree

	lines = min_qual.split("\n")
	for line in lines:
		if "degree" in line: #this line contains degree info
			#print line
			if "equivalent practical experience" in line:
				accept_prac_experience = True
			if "BA/BS" in line or "Bachelor's" in line: #min degree = Bachelor
				degrees.append("Bachelor")
			if "Master’s" in line or "MS" in line:
				degrees.append("Master")
			if "MBA" in line:
				degrees.append("MBA")
			if "JD" in line:
				degrees.append("JD")
			if "PhD" in line or "Doctor's" in line:
				degrees.append("Doctor")

	if "Bachelor" in degrees:
		min_degree = "Bachelor"
	elif "MBA" in degrees and "Master" not in degrees:
		min_degree = "MBA only"
	elif "MBA" in degrees and "Master" in degrees:
		min_degree = "MBA&Master"
	elif "MBA" not in degrees and "Master" in degrees:
		min_degree = "Master"
	elif "JD" in degrees:
		min_degree = "JD"
	elif "PhD" in degrees:
		min_degree = "PhD"
	else:
		min_degree = "N/A"
	return min_degree

def compare_degree(my_degree, degree):
    degree_rank = ["N/A", "Bachelor", "Master", "MBA&Master", "MBA only", "PhD", "JD"]
    if degree_rank.index(my_degree) >= degree_rank.index(degree):
        return 1
    else:
        return 0


def extract_degree_level_min_and_pref(min_array, pref_array):
	min_degs = []
	pref_degs = []
	for i in range(len(min_array)):
		min_deg = extract_min_degree(min_array[i])
		pref_deg = extract_min_degree(pref_array[i])
		
		if compare_degree(min_deg, pref_deg): #assign min_degree to pref_deg, if not mentioned in pref
			pref_deg = min_deg

		min_degs.append(min_deg)
		pref_degs.append(pref_deg)
	return min_degs, pref_degs








 
def compute_freq(text, N_gram):

	bigramfdist = FreqDist()
	threeramfdist = FreqDist()

	tokens = text.strip().split(' ')
	bigrams = ngrams(tokens,N_gram)
	bigramfdist.update(bigrams)
	return bigramfdist

def extract_title_ngram(temp, key_word, N_gram, tags, filteron, print_ngram, print_warning):
	
	pos_dict = dict()
	cat_titles = ""
	total_count = len(temp)
	count_key_word, unique_titles = 0, 0


	for i in range(len(temp)):
		#print temp.iloc[i]
		#if type(temp.iloc[i]) is float:
		#	tags[i] = "N/A"
		title = temp.iloc[i] #df.iloc[i]['Title']
		if key_word == "Intern":
			cond = "Intern" in title and "Internet" not in title and "Internal" not in title and "International" not in title
		elif key_word == "Engineer":
			cond = "Engineer" in title and "Engineering" not in title or "Engineer, Site Reliability Engineering" in title
		else: #if key_word in ["Manager", "Researcher", "Consultant", "Specialist", "Analyst", "Recruiter", "Administrator"]:
			cond = key_word in title




		if cond:
			count_key_word += 1
			if tags[i] is None:
				tags[i] = key_word
			else:
				#report warning
				#This position has been tagged 
				if print_warning:
					print "WARNING: This position (" + temp[i] + ") has been tagged for career level = " + tags[i] 
					print "Keep original tagging"
				count_key_word -= 1
				continue
			pos_dict.setdefault(key_word,[])
			if title not in pos_dict[key_word]:
				unique_titles += 1
				pos_dict[key_word].append(title)
				cat_titles += " , " + title
	
	
	if print_ngram == True:
		print "    %20s: %15s   %20s = %4d    %20s = %4d"%("SUMMARY", key_word, "Openings", count_key_word, "Unique titles", unique_titles)


	
	# Further edit "Intern" position by n-gram
	bigram_dict = dict()
	table = string.maketrans('()',',,')
	cat_titles = cat_titles.translate(table)
	title_phrases = cat_titles.split(",")
	

	for title_phrase in title_phrases:
		bigramfdist = compute_freq(title_phrase, N_gram)
		for biwords, count in bigramfdist.items():
			bigram = ""
			for i in range(len(biwords)):
				bigram += " " + biwords[i]
			bigram = bigram.strip()
			#bigram = biwords[0] + " " + biwords[1]
			bigram_dict.setdefault(bigram, 0)
			bigram_dict[bigram] += count 
	
	sorted_bigram_dict = sorted(bigram_dict.iteritems(), key=lambda (k,v): (v,k), reverse = True)
	if print_ngram:

		print "%30s  |   %s" % (str(N_gram) + "-Gram", "Occurence")
		print "----------------------------------------------------"
		for key, value in sorted_bigram_dict:
			if filteron == True:
				if key.split()[-1] == key_word:				
					print "%30s  |   %s" % (key, value)
			else:
				print "%30s  |   %s" % (key, value)
				
					
	#print count_key_word
	return count_key_word


def get_career_level_tags(array, mode = "tag mapping"):
	num = 0
	count_title = []
	
	if mode == "data exploration":
		tags = [None for i in range(len(array))]
		titles = ["Intern", "Manager", "Researcher", "Consultant", "Specialist", "Analyst", "Recruiter", "Administrator", "Investigator", "Strategist", "Engineer", "Partner", "Executive", "Scientist", "Lead", "Apprenticeship", "Teacher", "Counsel", "Assistant", "Head", "Architect", "Writer", "Chief of Staff", "Negotiator", "Representative", "Accountant", "Auditor", "Designer", "Advocate", "Associate", "Director", "Principal", "Advisor", "Linguist", "Trainer", "Controller", "Trader", "Copywriter", "Producer", "Editor", "Developer"]
		N_gram = 2
		for key_word in titles: #only 1 developer
			count = extract_title_ngram(array, key_word, N_gram, tags, False, False, False) #(64)
			count_title.append(count)
			num += count

		#corner cases
		#tags[236] = "Manager" #"Product Lifecycle Management"
		#tags[545] = "Intern" #Political Advertising Program, Summer-Fall 2018
		if "Product Lifecycle Management" in array[i]:
			tags[i] = "Manager"
		if "Political Advertising Program, Summer-Fall 2018" in array[i]:
			tags[i] = "Intern"
		
		#print num

	if mode == "tag mapping":
		tags = [None for i in range(len(array))]
		titles = ["Intern", "Manager", "Researcher", "Consultant", "Specialist", "Analyst", "Recruiter", "Administrator", "Investigator", "Strategist", "Engineer", "Partner", "Executive", "Scientist", "Lead", "Apprenticeship", "Teacher", "Counsel", "Assistant", "Head", "Architect", "Writer", "Chief of Staff", "Negotiator", "Representative", "Accountant", "Auditor", "Designer", "Advocate", "Associate", "Director", "Principal", "Advisor", "Linguist", "Trainer", "Controller", "Trader", "Copywriter", "Producer", "Editor", "Developer"]
		N_gram = 2
		for key_word in titles: #only 1 developer
			count = extract_title_ngram(array, key_word, N_gram, tags, False, False, False) #The only goal is to turn count here
			count_title.append(count)
			num += count

		#corner cases		
		for i in range(len(tags)):
			if "Product Lifecycle Management" in array[i]:
				tags[i] = "Manager"
			if "Political Advertising Program, Summer-Fall 2018" in array[i]:
				tags[i] = "Intern"


		career_level_maps = mmp.career_level_maps

		inverse_map = dict()
		for k, v in career_level_maps.iteritems():
			for i in v:
				inverse_map[i] = k
		#for k, v in inverse_map.iteritems():
			#print "%20s    %50s" %(k,v)
		
		for i in range(len(tags)):
			#print tags[i]
			tags[i] = inverse_map[tags[i]]	


	return tags





def extract_degree_ngram(temp, N_gram, tags, mode = "tag mapping"):
	
	if mode == "data exploration":
		print_ngram = True

		cat_exp_descriptions = ""

		for i in range(len(temp)): #range(len(temp)):

			if type(temp.iloc[i]) == float or temp.iloc[i] is None or temp.iloc[i] == "nan":
				valid_string = "N/A"
				print valid_string
				continue


			raw_description = temp.iloc[i]
			#print raw_description 


			description = raw_description.lower().split("\n")
			#print description
			for line in description:
				if "jd degree" in line:
					valid_string = "JD"
					return "JD degree"
				if "degree in" in line or "phd in" in line or "degree or" in line:
					if "degree in" in line:
						start = line.find("degree in") + 10
					if "phd in" in line:
						start = line.find("phd in") + 7
					if "degree or" in line:
						start = line.find("degree or") + 7
					if line.find("equivalent practical experience") != -1:
						end = line.find("equivalent practical experience")
					else:
						end = len(line)
					valid_string = line[start:end]
					valid_string = valid_string.replace(" or ",",").replace(", or",",").replace("an ", ", ").replace("a ",",")
					table = string.maketrans('()',',,')
					valid_string = valid_string.translate(table)					
					cat_exp_descriptions += valid_string
					print str(i) + " " + valid_string

		title_phrases = cat_exp_descriptions.split(",")
		bigram_dict = dict()

		for title_phrase in title_phrases:
			bigramfdist = compute_freq(title_phrase, N_gram)
			for biwords, count in bigramfdist.items():
				bigram = ""
				for i in range(len(biwords)):
					bigram += " " + biwords[i]
				bigram = bigram.strip()
				#bigram = biwords[0] + " " + biwords[1]
				bigram_dict.setdefault(bigram, 0)
				bigram_dict[bigram] += count 
	
		sorted_bigram_dict = sorted(bigram_dict.iteritems(), key=lambda (k,v): (v,k), reverse = True)
		if print_ngram:

			print "%30s  |   %s" % (str(N_gram) + "-Gram", "Occurence")
			print "----------------------------------------------------"
			for key, value in sorted_bigram_dict:	
				print "%30s  |   %s" % (key, value)

	if mode == "tag mapping":
		valid_string = "N/A"
		inverse_map = dict()
		for k, v in mmp.map_majors.iteritems():
			for i in v:
				inverse_map[i] = k
		#for k, v in inverse_map.iteritems():
			#print "%50s    %50s" %(k,v)
	
		for i in range(len(tags)):
			#get valid string

				if type(temp.iloc[i]) == float or temp.iloc[i] is None or temp.iloc[i] == "nan":
					valid_string = "N/A"
					#print valid_string
					#continue
				else:
					#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
					raw_description = temp.iloc[i]
					#print raw_description 


					description = raw_description.lower().split("\n")
					#print description
					for line in description:
						if "jd degree" in line:
							valid_string = "JD"
							return "JD degree"
						if "degree in" in line or "phd in" in line or "degree or" in line:
							if "degree in" in line:
								start = line.find("degree in") + 10
							if "phd in" in line:
								start = line.find("phd in") + 7
							if "degree or" in line:
								start = line.find("degree or") + 7
							if line.find("equivalent practical experience") != -1:
								end = line.find("equivalent practical experience")
							else:
								end = len(line)
							valid_string = line[start:end]
							valid_string = valid_string.replace(" or ",",").replace(", or",",").replace("an ", ", ").replace("a ",",")
							table = string.maketrans('()',',,')
							valid_string = valid_string.translate(table)
							#print i, valid_string
				#tagging for this valid_string

				#scan degree info sequentially, for further linear interpolation				

				marked = set()
				for k, v in inverse_map.iteritems():
					if v == 'A' or v == '/':
						continue
					if k in valid_string and v not in tags[i]:
						ind_k = valid_string.find(k)
						if k == "engineering" or k == "engineering field" or k == "engineering discipline":
							#if "engineering" not in tags[i] and "General - Engineering" not in tags[i]:
								#tags[i].append("General - Engineering")
							if "General - Engineering" not in marked:
								tags[i].append((ind_k, "General - Engineering"))
								marked.add("General - Engineering")
						else:
							#tags[i].append(v.strip())
							if v.strip() not in marked:
								tags[i].append((ind_k, v.strip()))
								marked.add("v.strip()")
				if valid_string == "N/A":
					tags[i] = ["N/A"]
				else:
					#sort tags[i]

					tags[i] = sorted(tags[i])
					for j in range(len(tags[i])):
						(ind_k, v) = tags[i][j]
						tags[i][j]= v
				#print tags[i]
	for i in range(len(tags)):
		if tags[i] == []:
			tags[i] = ["N/A"]
		#print tags[i]


	return
							


def extract_experience_years(min_qual):
	years = -1 # no info available
	if type(min_qual) == float or min_qual == "nan" or min_qual is None:
		years = -1
		return years 
	lines = min_qual.split("\n")
	for line in lines:
		if ("years of" in line or "year of" in line or "years experience" in line) and "penultimate" not in line: #this line contains degree info
			
			
			end = max(line.find("year of"), line.find("years of"), line.find("years experience"))
			start = end - 2
			# find the closest space
			while line[start] != " " and start > 0:
				start -= 1

			valid_string = line[start:end].replace("-", " ").replace("+"," ")
			if (int(valid_string) > years):
				years = int(valid_string) 
	return years

def extract_experience_years_min_and_pref(min_array, pref_array):
	min_years = []
	pref_years = []
	for i in range(len(min_array)):
		min_year = extract_experience_years(min_array[i])
		pref_year = extract_experience_years(pref_array[i])
		#print i, min_year, pref_year
		if pref_year < min_year: #-1 if not mentioned
			pref_year = min_year
		min_years.append(min_year)
		pref_years.append(pref_year)
	return min_years, pref_years
	





def extract_experience_area_ngram(temp, N_gram, tags, mode = "tag mapping"):
	
	if mode == "data exploration":
		print_ngram = True
	else: #"tag mapping mode"
		print_ngram = False
		inverse_map = dict()
		for k, v in mmp.experience_areas_map.iteritems():
			for i in v:
				inverse_map[i] = k
		#for k, v in inverse_map.iteritems():
			#print "%50s    %50s" %(k,v)

	cat_exp_descriptions = ""
	for i in range(len(temp)): #range(len(temp)):
		#print temp.iloc[i]
		if type(temp.iloc[i]) == float or temp.iloc[i] is None or temp.iloc[i] == "nan":
			valid_string = "N/A"
			#print valid_string
			continue

		raw_description = temp.iloc[i]
		#print raw_description 
		description = raw_description.lower().split("\n")
		#print description

		#print description
		for line in description:
			if "experience" in line or "king with" in line and "degree" not in line:
				#print line
				if "experience" in line:
					start = line.find("experience") + 10
				if "king with" in line:
					start = line.find("king with") + 9
				end = len(line)
				valid_string = line[start:end]
				#remove space before or after "/"
				valid_string = valid_string.replace(" / ", "/").replace(" /", "/").replace("/ ", "/")
				valid_string = valid_string.replace(" - ", "-").replace("- ", "-").replace(" -", "-")
				valid_string = valid_string.replace(" or ",",").replace(", or",",").replace(" an ", ", ").replace(" a ",",").replace(" and ", ",").replace(" and/or", ",").replace(" or ", ",").replace("either", ",").replace(" the", ",").replace(" in ", ",").replace(" with ",",").replace(" from ",",").replace(" at ", ",").replace(" using ", ",").replace(" such as", " ,"). replace (" to ", ", ").replace("through", ",").replace(" on ", ",").replace("using ", ",").replace(" like ",",").replace(" can ", ",").replace(" across ", ",").replace(" building ", ",").replace(" toward ", ",").replace( "including", ",").replace(" of ", ",").replace("more of",",")
				valid_string.replace("or",",").replace("experience in",",").replace("work in",",")
				table = string.maketrans('().:',',,,,')
				valid_string = valid_string.translate(table)					
				cat_exp_descriptions += valid_string
				#print str(i) + " " + valid_string
		# "tag mapping" - tag the descriptions
		if mode == "tag mapping":
			for k, v in inverse_map.iteritems():
				if k in valid_string and v not in tags[i] and v != " ":
					tags[i].append(v)
			if valid_string == "N/A":
				tags[i] = ["N/A"]

	if mode == "data exploration":	#sort and pring n-gram
		title_phrases = cat_exp_descriptions.split(",")
		bigram_dict = dict()

		for title_phrase in title_phrases:
			bigramfdist = compute_freq(title_phrase, N_gram)
			for biwords, count in bigramfdist.items():
				bigram = ""
				for i in range(len(biwords)):
					bigram += " " + biwords[i]
				bigram = bigram.strip()
				#bigram = biwords[0] + " " + biwords[1]
				bigram_dict.setdefault(bigram, 0)
				bigram_dict[bigram] += count 

		sorted_bigram_dict = sorted(bigram_dict.iteritems(), key=lambda (k,v): (v,k), reverse = True)
		if print_ngram: #"data exploration mode"

			print "%30s  |   %s" % (str(N_gram) + "-Gram", "Occurence")
			print "----------------------------------------------------"
			for key, value in sorted_bigram_dict:	
				print "%30s  |   %s" % (key, value)





