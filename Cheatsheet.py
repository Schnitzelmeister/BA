#RESETING INDEX
df.reset_index(drop=True)

#GET DATATYPES FOR COLUMNs
df.dtypes

#GET TYPE OF OBJECT
type(OBJECT)

#GET CURRENT DIRECTORY JUPYTER (import os)
os.getcwd()

#GET THE COUNT OF ROWS
df['column'].count()

#Grouping
#1. Apply the groupby function on a df and choose a variable
groups = df.groupby('Team')
#2. Now you have an object of type DataFrameGroupBy containing all the groups
#3. Extract the group you want, the extracted group is a dataframe
devils = groups.get_group('Devils')
