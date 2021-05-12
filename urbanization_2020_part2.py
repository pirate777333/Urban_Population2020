import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd

def splitstring(text):
    return text.split('[')[0]

df = pd.read_csv('D:/rektorov_rad/programirano/Urbanization_by_country_2020.csv')

df['Urban_Population%']=df['Urban_Population%'].apply(splitstring)
df['Urban_Population%']=pd.to_numeric(df['Urban_Population%'])

df['Urbanization_Rate%_15to20']=df['Urbanization_Rate%_15to20'].fillna('0')
df['Urbanization_Rate%_15to20']=df['Urbanization_Rate%_15to20'].apply(splitstring)
df['Urbanization_Rate%_15to20']=pd.to_numeric(df['Urbanization_Rate%_15to20'], errors='coerce')

trouble_nations={'Nauru':float('-0.06'),'Vatican City':float('-0.05'),'Bermuda':float('-0.44'),
                 'Puerto Rico':float('-0.14'),'Japan':float('-0.14'),'Andorra':float('-0.31'),                 
                 'Bulgaria':float('-0.22'),'Ukraine':float('-0.33'),'Latvia':float('-0.93'),'Lithuania':float('-0.31'),
                 'Poland':float('-0.25'),'Croatia':float('-0.08'),'Serbia':float('-0.07'),
                 'Moldova':float('-0.07'),'Samoa':float('-0.47'),'Romania':float(0)}

for i,r in df.iterrows():
    if df.iloc[i,0] in trouble_nations:
       df.iloc[i,-1] = trouble_nations[df.iloc[i,0]]

#df['Urbanization_Rate%_15to20']=df['Urbanization_Rate%_15to20'].fillna(0)
#print (df[pd.to_numeric(df['Urbanization_Rate%_15to20'], errors='coerce').isnull()])
#print(df.columns)
#print(df.head(13))
#print(df.shape)
#print(df.dtypes)

df=df.sort_values(by='Urban_Population%', ascending=False)
print(df.iloc[:20,:])

fig=px.bar(df.iloc[0:20],y='Urban_Population%',x='Nation',color='Nation',
           text='Urban_Population%',template='plotly_dark',title='(Highest) Urban Population in %')
fig.show()

df=df.sort_values(by='Urban_Population%', ascending=True)
print(df.iloc[:20,:])

fig=px.bar(df.iloc[3:23],y='Urban_Population%',x='Nation',color='Nation',
           text='Urban_Population%',template='plotly_dark',title='(Lowest) Urban Population in %')
fig.show()

df=df.sort_values(by='Urbanization_Rate%_15to20', ascending=False)
print(df.iloc[:20,:])

fig=px.bar(df.iloc[0:20],y='Urbanization_Rate%_15to20',x='Nation',color='Nation',
           text='Urbanization_Rate%_15to20',template='plotly_dark',title='(Highest) Urbanization rate in % from 2015 to 2020')
fig.show()

df=df.sort_values(by='Urbanization_Rate%_15to20', ascending=True)
print(df.iloc[:15,:])

fig=px.bar(df.iloc[0:20],y='Urbanization_Rate%_15to20',x='Nation',color='Nation',
           text='Urbanization_Rate%_15to20',template='plotly_dark',title='(Lowest) Urbanization rate in % from 2015 to 2020')
fig.show()

df = df[(df.Nation != 'nan')]
df = df[(df.Nation != 'South Sudan')]
df = df[(df.Nation != 'Wallis and Futuna')]
#&(df.Nation != 'South Sudan')&(df.Nation != 'Wallis and Futuna')]
print(df.shape)
world_map=gpd.read_file("D:/desktop_things/Diplomski/3/GeoViz/esej/World_Map.shp")
print(world_map.head())
print(world_map.shape)
print(world_map.dtypes)



world_map.replace("Burma","Myanmar",inplace=True)
world_map.replace("Netherlands Antilles","Curaçao",inplace=True)
world_map.replace("Cote d'Ivoire","Ivory Coast",inplace=True)
world_map.replace("Korea, Republic of","South Korea",inplace=True)
world_map.replace("Falkland Islands (Malvinas)","Falkland Islands",inplace=True)
world_map.replace("United Republic of Tanzania","Tanzania",inplace=True)
world_map.replace("Holy See (Vatican City)","Vatican City",inplace=True)
world_map.replace("United States Virgin Islands","U.S. Virgin Islands",inplace=True)
world_map.replace("Saint Helena","Saint Helena, Ascension and Tristan da Cunha",inplace=True)
world_map.replace("Brunei Darussalam","Brunei",inplace=True)
world_map.replace("Iran (Islamic Republic of)","Iran",inplace=True)
world_map.replace("Micronesia, Federated States of","F.S. Micronesia",inplace=True)
world_map.replace("Korea, Democratic People's Republic of","North Korea",inplace=True)
world_map.replace("Saint Martin","Sint Maarten",inplace=True)
world_map.replace("Sao Tome and Principe","São Tomé and Príncipe",inplace=True)
world_map.replace("Syrian Arab Republic","Syria",inplace=True)
world_map.replace("Republic of Moldova","Moldova",inplace=True)
world_map.replace("Viet Nam","Vietnam",inplace=True)
world_map.replace("Lao People's Democratic Republic","Laos",inplace=True)
world_map.replace("Swaziland","Eswatini",inplace=True)
world_map.replace("Libyan Arab Jamahiriya","Libya",inplace=True)
world_map.replace("Democratic Republic of the Congo","DR Congo",inplace=True)
world_map.replace("The former Yugoslav Republic of Macedonia","North Macedonia",inplace=True)


##for i,r in df.iterrows():
##    if df.iloc[i,0] not in world_map['NAME'].to_list():
##        print(df.iloc[i,0])
##
##print('end')
df.columns=['NAME','Urban_Population%','Urbanization_Rate%_15to20']
#merge=world_map.join(df,on="NAME", how="right")
merge=pd.merge(world_map, df, on='NAME')
print(merge)
merge=merge.set_geometry('geometry')
ax=merge.plot(column="Urban_Population%",
              cmap="OrRd",
              figsize=(15,15),
              legend=True,
              scheme="user_defined",
              classification_kwds={"bins":[20,40,60,80,100]},
              edgecolor="black",
              linewidth=0.5)
ax.set_title("Urban Population in %", fontdict={'fontsize':20})

ax.set_axis_off()

ax.get_legend().set_bbox_to_anchor((0.18, 0.6))

plt.show()
