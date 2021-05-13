import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd

df = pd.read_csv('D:/rektorov_rad/programirano/Urbano/2a6181d4-c7db-478f-acac-2eafe10aabc2_Data.csv')
df=df.iloc[:-52,2:-1]

df.columns=['Country Name', 'Country Code', '1990', '2000',
            '2011', '2012', '2013', '2014', '2015', '2016',
            '2017', '2018', '2019']

def stringops(text):
    if text=='..':
        return None
    else:
        return text

for i in df.columns:
    df[i]=df[i].apply(stringops)

df=df.dropna()

#print(df.isnull().sum())

lista=['1990', '2000',
            '2011', '2012', '2013', '2014', '2015', '2016',
            '2017', '2018', '2019']

for i in lista:
    df[i]=pd.to_numeric(df[i])

#print(df.dtypes)

print(df.shape)

print(df.head())

df=df.sort_values(by='2019', ascending=False)
print(df.iloc[:10,:])

fig=px.bar(df.iloc[0:10],y='2019',x='Country Name',color='Country Name',
           text='2019',template='plotly_dark',title='(Highest) Population in largest city')
fig.show()

df=df.sort_values(by='2019', ascending=True)
print(df.iloc[:10,:])

fig=px.bar(df.iloc[0:10],y='2019',x='Country Name',color='Country Name',
           text='2019',template='plotly_dark',title='(Lowest) Population in largest city')
fig.show()


def specific_country(country_name):
    country_data = df[df['Country Name']==country_name]
    country_data=country_data.T
    country_data=country_data.iloc[2:,:]
    year=country_data.index.tolist()
    data=country_data.iloc[:,0].tolist()
    fig=px.bar(y=data,x=year,color=year,
           template='plotly_dark',title=country_name+' Population in largest city',
           labels=dict(x="Years", y="Population in largest city", color="Years"))
    fig.show()
    fig=px.line(y=data,x=year,
           template='plotly_dark',title=country_name+' Population in largest city',
           labels=dict(x="Years", y="Population in largest city"))
    fig.show()

a=input('Your Country Name: __ ')

try:
    specific_country(a)
except:
    print('Invalid Country Name')





df['90_00']=(df['2000']/df['1990'])-1
df['00_11']=(df['2011']/df['2000'])-1
df['11_19']=(df['2019']/df['2011'])-1
df['90_19']=(df['2019']/df['1990'])-1
print(df.head())

df=df.sort_values(by='90_19', ascending=False)
print(df.iloc[:10,:])

fig=px.bar(df.iloc[0:10],y='90_19',x='Country Name',color='Country Name',
           text='90_19',template='plotly_dark',title='(Highest) Population growth in %')
fig.show()

df=df.sort_values(by='90_19', ascending=True)
print(df.iloc[:10,:])

fig=px.bar(df.iloc[0:10],y='90_19',x='Country Name',color='Country Name',
           text='90_19',template='plotly_dark',title='(Lowest) Population growth in %')
fig.show()
