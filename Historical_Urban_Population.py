import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd

df = pd.read_csv('D:/rektorov_rad/programirano/Urbano/92f09b53-3a44-4516-ba50-789d5d7553fe_Data.csv')
df=df.iloc[:-5,2:-1]
df.columns=['Country Name', 'Country Code', '1990', '2000',
            '2011', '2012', '2013', '2014', '2015', '2016',
            '2017', '2018', '2019']
lista=['1990', '2000',
            '2011', '2012', '2013', '2014', '2015', '2016',
            '2017', '2018', '2019']

df = df[df['Country Name'] != 'Eritrea']
df = df[df['Country Name'] != 'Kosovo']
df = df[df['Country Name'] != 'St. Martin (French part)']
df = df[df['Country Name'] != 'Not classified']


df['1990']=pd.to_numeric(df['1990'])
df['2000']=pd.to_numeric(df['2000'])
df['2011']=pd.to_numeric(df['2011'])
df['2012']=pd.to_numeric(df['2012'])
df['2013']=pd.to_numeric(df['2013'])
df['2014']=pd.to_numeric(df['2014'])
df['2015']=pd.to_numeric(df['2015'])
df['2016']=pd.to_numeric(df['2016'])
df['2017']=pd.to_numeric(df['2017'])
df['2018']=pd.to_numeric(df['2018'])
df['2019']=pd.to_numeric(df['2019'])

#print(df.dtypes)
#print(df.head())
#print(df.shape)
#print(df.isnull().any())
#print(df[df.isnull().any(axis=1)])

df=df.sort_values(by='2019', ascending=False)
world=df.iloc[0,:].to_frame()
world=world.iloc[2:,:]
#print(world)
#print(world.index)
x=world.index.tolist()
y=world.iloc[:,0].tolist()
#print(x,y)
china=df.iloc[15,:]
india=df.iloc[23,:]
usa=df.iloc[36,:]
#print(world)
#print(china)
#print(india)
#print(usa)
df=df.iloc[44:,:]
df = df[df['Country Name'] != 'Central Europe and the Baltics']
df = df[df['Country Name'] != 'Small states']
df = df[df['Country Name'] != 'Other small states']
df = df[df['Country Name'] != 'Caribbean small states']
df = df[df['Country Name'] != 'Pacific island small states']
df=df.append(china)
df=df.append(india)
df=df.append(usa)
print('SHAPE       ',df.shape)
df=df.sort_values(by='2019', ascending=False)


print(df.iloc[:10,:])

fig=px.bar(df.iloc[0:10],y='2019',x='Country Name',color='Country Name',
           text='2019',template='plotly_dark',title='(Highest) 2019 Urban population')
fig.show()

fig=px.bar(y=y,x=x,color=x,
           template='plotly_dark',title='World Urban population',
           labels=dict(x="Years", y="Urban Population", color="Years"))
fig.show()

def specific_country(country_name):
    country_data = df[df['Country Name']==country_name]
    country_data=country_data.T
    country_data=country_data.iloc[2:,:]
    year=country_data.index.tolist()
    data=country_data.iloc[:,0].tolist()
    fig=px.bar(y=data,x=year,color=year,
           template='plotly_dark',title=country_name+' Urban population',
           labels=dict(x="Years", y="Urban Population", color="Years"))
    fig.show()

a=input('Your Country Name: __')

try:
    specific_country(a)
except:
    print('Invalid Country Name')

df=df.sort_values(by='2019', ascending=True)

print(df.iloc[:10,:])

fig=px.bar(df.iloc[0:10],y='2019',x='Country Name',color='Country Name',
           text='2019',template='plotly_dark',title='(Lowest) 2019 Urban population')
fig.show()

df=df.sort_values(by='2019', ascending=False)

df = pd.melt(df, id_vars=['Country Name', 'Country Code'], value_vars=lista)
print(df)
fig = px.choropleth(df,                            # Input Dataframe
                     locations="Country Code",           # identify country code column
                     color="value",                     # identify representing column
                     hover_name="Country Name",              # identify hover name
                     animation_frame="variable",        # identify date column
                     projection="natural earth",        # select projection
                     color_continuous_scale = 'Peach',  # select prefer color scale
                     range_color=[0,800000000]              # select range of dataset
                     )        
fig.show()
