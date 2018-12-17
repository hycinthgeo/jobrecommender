# jobrecommender
This job recommender system was built in fall 2018, for the partial fulfillment of CS410 - Text Information System. 

# How to install? 
### Download from https://github.com/hycinthgeo/jobrecommender
### Activate one of the two optional user interfaces 
  - Option 1: Terminal access: type "cd jobrecommender", then type "python main.py"
  - Option 2: Jupyter Notebook access: type ""cd jobrecommender", then type "jupyter notebook". Click into the "main_UI_final.ipynb"

### The following figure briefly introduced the file folder structure, where 
  - The main function communicates with the /database/ and /recommender/ subfolders.
  - Software requirement are documented in requirements.txt 
  - Supporting documents are also included, such as the figures, test case, and the /data_exploration/ folder, which detailed the process of identifying the frequent and meaningful N-grams, which are further extracted as the tags to further labeling educations and experience/skills.
![alt text](https://github.com/hycinthgeo/jobrecommender/blob/master/figs/Figure_folder_files.png)


# How it works? 

### As illustrated in the following figure, this job recommender mainly contains two components, namely 
  - The pre-processing module. This module cleaned and tagged and raw data, by using the 300+ tags that I revealed during the data exploration. 
  - The user's query interface, where the user is gradually guided to his/her interested jobs by two rounds of queries. 
![alt text](https://github.com/hycinthgeo/jobrecommender/blob/master/figs/Figure_workflow.png)

### The job recommendation is made via content-based filtering and ranking. 
  - An example as below further detailed how it works. 
  
# Example of an use case 
The following shows an example of use case. 
A volunteer, who contributed to my product survey, kindly agreed me to share this example. 
![alt text](https://github.com/hycinthgeo/jobrecommender/blob/master/figs/Figure_Example_Use_Case.png)

This job recommender system inquires the user's info and preferences via two rounds of queries. 
  - The first round only queries for fundamental basic information on job position, working experience (years), and preferred locations.
  - Then present the user a summary of job requirements for jobs that the user (1) meets the minimum qualification, or (2) the preferred qualification. 
  - In this example, the user chose the match_level = "min", thus would see more job openings with less strict filtering. 
  - In the second round of queries. The user started to answer more detailed questions on their highest degree, studied majors, interested and uninterested skills that are related to this job, and his/her previous responsibilities. 
  
Eventually, the system computed three scaled score to respectively represent 
  - How matched his/her academic background is
  - How matched his/her interested skills are, discounted by his/her uninterested skills
  - How similar his/her previous responsibilities are compared to this job
  
These three metrics are averaged to obtain a final score for top 10 ranking, by assuming the employer values the education, skills and responsibilities in the same manner. 

Finally, the figure on the right bottom plotted out the scores in 3D, and listed the top ranked jobs. If an user is interested to dig into any of them, he/she can easily retrieve the original skill post by typing the corresponding rank number. 
