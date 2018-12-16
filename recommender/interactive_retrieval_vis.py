import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D

import helper_mapping_dictionaries as mmp

small_fontsize = 10


# visualize results for first output

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


def get_degree(df, mode):
	df3 = attribute_counter(df['tag_'+ mode +'_degree_type'], 'Degree_Level')
	category = list(df3['Degree_Level'])
	perc = list(df3['Count'])
	perc = [100*i /sum(perc) for i in perc]
	return df3, category, perc

def get_sorted_degree_area(df, mode):
	#--------------------------------------------Degree Areas --------------------------------------------------------
	df4 = long_attribute_counter(df['tag_'+ mode +'_degree_areas'], 'Degree_Area')
	#print df4
	df4_sorted = df4.sort_values(['Count'], ascending=[1])

	#----------------------------------------Set shared colormap ------------------------------------------------------
	map_majors = mmp.map_majors
	#print map_majors.keys()

	map_major_colors = mmp.map_major_colors

	#color_array = ['r','y','b','g','b','c','m']
	color = []
	for i in range(len( df4_sorted['Degree_Area'])):
		j = 0
		for k, v in map_majors.iteritems():
			if df4_sorted.iloc[i]['Degree_Area'] == k:
				#color.append(color_array[j %len(color_array)])
				color.append(map_major_colors[df4_sorted.iloc[i]['Degree_Area']])
			j += 1

	return df4_sorted, color

def get_sorted_skills(df, mode):
	df5 = long_attribute_counter(df['tag_'+ mode +'_exp_skills'], 'Exp/Skills')
	df5 = df5[df5['Exp/Skills'] != " "]
	df5_sorted = df5.sort_values(['Count'], ascending=[0])
	df5_sorted = df5_sorted.reset_index().drop(['index'], axis = 1)
	#print df5_sorted
	return df5_sorted



def first_round_user_query_visualization(df, plot_flag, fig_dir_path):
	if plot_flag == 'min':
		title_prefix = "Minimum"
	else:
		title_prefix = "Preferred"
	


	df3, category, perc = get_degree(df, plot_flag)
	df4_sorted, color = get_sorted_degree_area(df, plot_flag)
	df5_sorted = get_sorted_skills(df, plot_flag)
	#print df5_sorted
	#df5_sorted = df5_sorted.head(10)

	# Create 2x2 sub plots
	pie_colors = [[183, 183, 183], [230, 252, 209], [252, 230, 174],[168, 247, 239],[255, 188, 122], [214, 198, 255], [255, 226, 242] ]
	
	pie_colors = [[pie_colors[i][0]/255.0,pie_colors[i][1]/255.0, pie_colors[i][2]/255.0] for i in range(len(pie_colors))]

	gs = gridspec.GridSpec(2, 2)
	#plot pie chart for degree
	fig = pl.figure(figsize=(18,12))
	ax = pl.subplot(gs[0, 0]) # row 0, col 0
	n = pl.pie(perc, labels = category, colors = pie_colors[:len(category)], startangle=90, autopct='%.1f%%', textprops={'fontsize': small_fontsize })
	ax.set_aspect('equal')
	pl.title(title_prefix + " Qualifications - Degree", fontsize = 20, fontweight = 'bold')
	
	# plot bar chart for degree areas
	ax = pl.subplot(gs[0, 1]) # row 0, col 1
	objects = df4_sorted["Degree_Area"]
	y_pos = np.arange(len(objects))
	performance = df4_sorted["Percent"]	 
	pl.barh(y_pos, performance, align='center', alpha=0.5, color = tuple(color))
	pl.yticks(y_pos, objects, rotation = 0, fontsize = small_fontsize )
	pl.xlabel('Percent %', fontsize = 14)
	pl.xlim([0, 100])
	pl.title('Degree Majors', fontsize = 20, fontweight = 'bold')
	#pl.rcParams.update({'font.size': 8})


	ax = pl.subplot(gs[1, :]) # row 1, span all columns
	df5_sorted = df5_sorted.iloc[:15]
	df5_sorted = df5_sorted.sort_values(['Count'], ascending=[1])

	objects = df5_sorted["Exp/Skills"]
	y_pos = np.arange(len(objects))
	performance = df5_sorted["Percent"]
	 
	pl.barh(y_pos, performance, align='center', alpha=0.5)
	pl.yticks(y_pos, objects, rotation = 0, fontsize = small_fontsize )
	pl.xlabel('Percent %', fontsize = 14)
	pl.xlim([0, 30])
	pl.title('Top 15 Exp/Skills', fontsize = 20, fontweight = 'bold')
	pl.show()
	#fig.savefig(fig_dir_path + "Summary_jobs_meet_" + plot_flag +"_qualifications")

# plot 3D results 
def plot_3D_results(xs, ys, zs, labels, titles, locs, fig_dir_path):
    fig = plt.figure(figsize = (18, 15))
    ax = fig.add_subplot(111, projection='3d')

    i = 0
    for j in range(len(xs)):
        for c, m in [('b', 'o')]:
            #print labels[i]
            s = 1.0/(labels[i] + 1) * 100
            ax.scatter(xs[j], ys[j], zs[j], c=c, marker=m, s= s)
            i += 1

    ax.set_xlabel('Scaled score 1: Resp. similarity', fontsize = 14)
    ax.set_ylabel('Scaled score 2: Skill match', fontsize = 14)
    ax.set_zlabel('Scaled score 3: Major match', fontsize = 14)

    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])
    
    #plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    #plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

    #print plt.rcParams.keys()

    zdirs = [None for i in range(len(xs))]

    count = 0
    for zdir, x, y, z, label in zip(zdirs, xs, ys, zs, labels):
        label = '%3s' % (label)
        ax.text(x, y, z, label, zdir, fontsize = 12)
        count += 1
	plt.title('Top 10 Recommended Jobs', fontsize = 20, fontweight = 'bold', loc = 'left')
    

	legends = [None for i in range(len(titles))]
	for i in range(len(labels)):
		title = titles[i].split(",")
		legends[i] = "%3s - %s - %20s" %(str(labels[i]), title[0].strip(), locs[i])
	#print legends
    
    	#set legend positions
    box = ax.get_position()
    print [box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9]
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

    #ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=1)
    
    plt.legend(legends)

    plt.show()
    fig.savefig(fig_dir_path + "Final_recommended_top10_jobs.png")
	





# lookup_a_recommended_job(df_top10) 



