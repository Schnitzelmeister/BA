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

#Convert one particular column to datetime-format //NOT possible for STRING
df['ValueDate'] = pd.to_datetime(df['ValueDate'])

#Convert one particulat column to String
total_rows['ColumnID'] = total_rows['ColumnID'].astype(str)

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

#Suppressing Warnings Jupyter
import warnings
warnings.filterwarnings('ignore')

#Round up a Float
import math
print(math.ceil(4.2))

#Convert a column in a DF
df['column'].astype('category')

#Group by month using a Grouper
df.groupby(pd.Grouper(freq='M'))

#Group by without using a Grouper
df.groupby(by=[b.index.month, b.index.year]) #The index most likely has to be a datetimeindex

#Set specific column as index
df = df.set_index('Datetime') / df.index = df['column']

#Einen Dataframe aus einem JSON File erstellen
#1. Man öffnet die Datei - passendes Encoding !!!
#2. Danach konvertiert man das Ganze in einen Dict (Ganz wichtig zu wissen wie man die Elemente im Dict accessed)
#3. Als letzten Schritt hat man den 
#Alles außer Nummer ist ein object da Pandas auf Numpy aufgebaut, also beispielsweise auch String ist ein object. Es gibt keinen String Typ in Pandas
data_file = open('CityBikeWien/Stationendaten.json', encoding='UTF-8') 
json_dict = json.load(data_file)
stations_dataframe = pd.DataFrame(json_dict['stations']['station'])



