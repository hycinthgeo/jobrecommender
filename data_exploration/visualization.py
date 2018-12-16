import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np
import operator

richcolors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in richcolors.items())
sorted_names = [name for hsv, name in by_hsv]



def display_pie_chart(df, attribute, title):
	category_all = list(set(df[attribute]))
	perc_all = [1.0 * (len(df[df[attribute] == category_all[i]]))/len(df) * 100 for i in range(len(category_all))] 
	colors = ['r','g','b','y','c','r','g','b','y','c','r','g','b','y','c','r','g','b','y','c']
	colors = colors[:len(df[attribute])]
	#print category_all, perc_all, colors
	#print perc_all

	plt.pie(perc_all, labels=category_all, colors=colors, startangle=90, autopct='%.1f%%')
	if title != "":
		plt.title(title)
		plt.show()
	return



def display_education_pie_chart(df, attribute1, attribute2):
	plt.figure()
	plt.subplot(131)
	display_pie_chart(df, attribute1,"")
	#plt.subplot(132)
	#display_pie_chart('min_degrees_accept_prac_exp')
	plt.subplot(132)
	display_pie_chart(df, attribute2,"")
	plt.show()
	return

def display_title_career_level(array):
	plt.figure()
	category_all = sorted(list(set(array)))
	#print category_all
	
	count=[0 for i in range(len(category_all))]
	for i in range(len(category_all)):
		for j in range(len(array)):
			if array[j] == category_all[i]:
				count[i] += 1 
	perc_all = [1.0 * count_i/len(array) for count_i in count]

	#perc_all = [1.0 * (len(array[array == category_all[i]]))/len(array) * 100 for i in range(len(category_all))]
	#rainbow = ['salmon','moccasin','gold','aquamarine','deepskyblue','cyan','orchid']
	#rainbow = [richcolors[str(color_name)] for color_name in rainbow]
	#rainbow = ['#FA8072','#FFE4B5','#FFD700','#7FFFD4','#00BFFF','#00FFFF','#DA70D6']
	#rainbow = [[128, 128, 128],[0, 0, 128]]
	rainbow = ['r','g','b','y','c','r','g','b','y','c','r','g','b','y','c','r','g','b','y','c','r','g','b','y','c']
	colors = rainbow[:len(perc_all)]
	plt.pie(perc_all, labels=category_all, colors=colors, startangle=90, autopct='%.1f%%')
	plt.show()

def display_major_tags(df, attribute, title):	
	#print degree_tags
	
	major_counter = dict()
	for i in range(len(df)):
		for major in df.iloc[i][attribute]:
			if major != "N/A":
				major_counter.setdefault(major,0)
				major_counter[major] += 1
	
	
	major_counter = sorted(major_counter.items(), key=operator.itemgetter(1), reverse = False)
	perc = [0 for i in range(len(major_counter))]
	objects = [0 for i in range(len(major_counter))]
	colors = [0 for i in range(len(major_counter))]
	labels = [0 for i in range(len(major_counter))]
	for i in range(len(major_counter)):
		(k, v) = major_counter[i]
		perc[i] = 1.0 * v/len(df) * 100
		objects[i] = k
		if "General" in k:
			colors[i] = 'grey'
		else:
			colors[i] = 'blue'
		labels[i] = str(perc[i]) + "%"
	#colors = tuple(colors)


	i = 0

	"""
	for major, count in major_counter.iteritems():
		perc[i] = count/(1.0 *len(df)) #convert to percentage
		objects[i] = major
		i += 1
	print perc
	"""
	objects = tuple(objects)
	y_pos = np.arange(len(objects))
	performance = perc

	plt.barh(y_pos, performance, align='center', alpha=0.5, color=colors)
	plt.yticks(y_pos, objects)
	plt.xlabel('Percentage of all jobs')
	plt.title(title)
	plt.show()


	""" 
# Text on the top of each barplot
	for i in range(len(labels)):
		plt.text(x = 100 , y = 20, s = labels[i], size = 6)

	plt.show()
	"""
	


#Final percentage stacked bar plot
#each category a bar to show required degree ??
	
		
