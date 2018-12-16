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


  

