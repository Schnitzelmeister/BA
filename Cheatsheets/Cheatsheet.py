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

#Aggregation auf Gruppierung
aggregation_devils = devils['Spalte'].agg(np.aggregatFunktion)

#Example Query
import seaborn as sns

titanic = sns.load_dataset('titanic')

titanic[
    (titanic['sex'] == 'female')
  & (titanic['class'].isin(['First', 'Third']))
  & (titanic['age'] > 30)
  & (titanic['survived'] == 0)
]

#Convert one particular column to datetime-format
df['ValueDate'] = pd.to_datetime(df['ValueDate'])

# Set the Date as Index
df.index = df['ValueDate']

#Truncate Date (drops hours minutes and seconds/miliseconds)
df['starttime'].apply(lambda x: x.date())

#get number of unique values in column
df['trip_id'].nunique

#Resizing Figures
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10.0
fig_size[1] = 7.0

#Convert Series to DataFrame
#Die Funktion to_frame returniert ein DataFrame mit dem Spaltennamen count
series_object.to_frame('SOLL-SpaltenName') 

#Drop column(s) dataframe
df.drop(['B', 'C'], axis=1)

#Define a Timedelta-Object
pd.Timedelta('120 sec') 

_________________________MARKDOWN FOR JUPYTER NOTEBOOK_________________________
