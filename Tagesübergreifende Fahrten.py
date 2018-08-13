import pandas
from datetime import datetime

#Fahrtdaten werden aus CSV gelesen und das Datum gleichzeitig geparst
df = pandas.read_csv('trip.csv', error_bad_lines=False, parse_dates=['starttime', 'stoptime'])

#Funktion zur Anpassung der Daten
def extract_date(date):
    return datetime.strptime(str(date.year)+str(date.month)+str(date.day),'%Y%m%d')
        
#Die Studen:Minuten:Sekunden:Milisekunden werden gedroppt        
df[['starttime','stoptime']] = df[['starttime','stoptime']].apply(lambda x: x.apply(extract_date))

#Die Anzahl der Non-Null Werte wird überprüpft ob diese bei beiden Spalten übereinstimmen | JA stimmen überein
df['starttime'].notnull
df['stoptime'].notnull


count = 0
for row_index,row in df.iterrows():
    if(row['starttime'] != row['stoptime']):
        count += 1
   
#Absolute Anzahl der tagesübergreifenden Fahrten        
print(count)

#Relativer Anteiler an tagesübergreifenden Daten verglichen mit Gesamtanzahl an Fahrten
count/286857 ~ 0.0027 = 0,27 % 