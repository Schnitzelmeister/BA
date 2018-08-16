import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Daten werden gelesen
df = pd.read_csv('trip.csv', error_bad_lines=False, parse_dates=['starttime', 'stoptime'])

#Visualisierungseinstellungen mithilfe von Seaborn
sns.set(color_codes = True)

#Die beiden Spalten werden gezogen
df_short = df[['trip_id','starttime']]

#Der Index wird mit dem Datum ersetzt
df_short.index = df_short.starttime

#Das DataFrame wird in eine Serie konvertiert
df_short = df_short.trip_id

#Es werden die Gruppen je Monat erstellt
monthly_groups = df_short.groupby(pd.Grouper(freq='M'))

#Die Anzahl der Fahrten innerhalb der Gruppen(=Monaten) wird summiert
no_rides_each_month = monthly_groups.agg(np.size)

jahr_eins = no_rides_each_month[:12]
jahr_zwei = no_rides_each_month[12:]

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10.0
fig_size[1] = 7.0

#Beide plots einstellen
jahr2014 = plt.bar(np.arange(12), jahr_eins, width= 0.4, color = 'g')
jahr2015 = plt.bar(np.arange(11)+0.4, jahr_zwei, width= 0.4, color = 'b')


plt.xticks(index,  
          ('Okt','Nov','Dez','Jan','Feb',
           'Mar','Apr','Mai','Jun','Jul','Aug','Sep'))

plt.show()